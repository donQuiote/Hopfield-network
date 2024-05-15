import numpy as np
from Main_classes import Utilities as ut
import pytest
import doctest
from pathlib import Path
import os
import shutil
from Main_classes import HopfieldNetwork as hopfn
from Main_classes import DataSaver as dsv
from Main_classes import Pattern_handler as Paha

#=================Tests from Hopfield=================
Generator = Paha.Pattern_handler()
Ut = ut.Utilities()

def test_HopfieldNetwork__init__():
    with pytest.raises(NameError):
        Hopf_netwk = hopfn.HopfieldNetwork([1],'NameError')

def test_generate_patterns():
    #Tests if the function returns a matrix with elements of value either 1 or -1
    assert np.all([[y == 1 or y == -1 for y in a_pattern] for a_pattern in Generator.generate_patterns(10, 20)])
    #Tests if the mtrix returned is of correct size
    assert np.shape(Generator.generate_patterns(5, 15)) == (5, 15)
    #Tests for checking the input of the function
    with pytest.raises(ValueError):
        Generator.generate_patterns(-1, 0)
    with pytest.raises(ValueError):
        Generator.generate_patterns(0.3, 3)
    with pytest.raises(OverflowError):
        Generator.generate_patterns(1e300, 3)

def test_perturb_pattern():
    pattern = Generator.generate_patterns(1, 10)
    #Tests if the correct number of perturbation occured
    assert np.all(Generator.perturb_pattern(pattern[0], 0) == pattern)
    assert np.all(Generator.perturb_pattern(pattern[0], 10) == -pattern)
    assert (Generator.perturb_pattern(pattern[0], 3) == pattern).sum() == 7

def test_pattern_match():
    #Tests if a matrix containing a pattern correponding to the pattern as second argument is correctly identified
    patterns = Generator.generate_patterns(40, 100)
    assert Generator.pattern_match(patterns, patterns[32]) == 32
    #Tests if the memorized_patterns fit the input requirements
    with pytest.raises(ValueError):
        Generator.pattern_match(np.array([[1, 4],[1, -1]]), np.array([1, 1]))

def test_hebbian_weights():
    patterns = Generator.generate_patterns(5, 10)
    Hopf_netwk = hopfn.HopfieldNetwork(patterns)
    # Tests that the size of the Hebbian weights matrix is correct
    assert np.size(Hopf_netwk.weights) == 100
    # Tests that the values of the matrix are in the correct range
    assert np.all([[y <= 1 and y >= -1 for y in line] for line in Hopf_netwk.weights])
    # Tests if the matrix is symmetric
    assert np.allclose(Hopf_netwk.weights, Hopf_netwk.weights.T)
    # Tests that all the elements in the diagonal of the matrix are equal to 0
    assert np.all(Hopf_netwk.weights[i][i] == 0. for i in range(np.shape(Hopf_netwk.patterns)[1]))
    #Test if we get an expected output for a certain pattern
    Hopf_netwk = hopfn.HopfieldNetwork(np.array([[1,1,-1,-1],[1,1,-1,1],[-1,1,-1,1]]))
    assert np.allclose(Hopf_netwk.weights,np.array([[0,0.33333333,-0.33333333,-0.33333333],[0.33333333,0,-1,0.33333333],[-0.33333333,-1,0,-0.33333333],[-0.33333333,0.33333333,-0.33333333,0]]))
    #Tests if patterns fit the input requirements
    with pytest.raises(ValueError):
        Hopf_netwk = hopfn.HopfieldNetwork(np.array([[1, 4],[1, -1]]))

def test_storkey_weights():
    patterns = Generator.generate_patterns(5, 10)
    Hopf_netwk = hopfn.HopfieldNetwork(patterns,'storkey')
    #Test that the size of the Storkey weights matrix is correct
    assert np.size(Hopf_netwk.weights) == 100
    #Test if the matrix is symmetric
    assert np.allclose(Hopf_netwk.weights,Hopf_netwk.weights.T)
    #Test if we get an expected output for a certain pattern
    Hopf_netwk = hopfn.HopfieldNetwork(np.array([[1,1,-1,-1],[1,1,-1,1],[-1,1,-1,1]]), 'storkey')
    assert np.allclose(Hopf_netwk.weights, np.array([[1.125,0.25,-0.25,-0.5],[0.25,0.625,-1.,0.25],[-0.25,-1.,0.625,-0.25],[-0.5,0.25,-0.25,1.125]]))
    #Tests if patterns fit the input requirements
    with pytest.raises(ValueError):
        Hopf_netwk = hopfn.HopfieldNetwork(np.array([[1, 4],[1, -1]]), 'storkey')

def test_update():
    state = np.array([-1, 1, -1, -1])
    Hopf_netwk = hopfn.HopfieldNetwork(Generator.generate_patterns(3,4))
    #Test if the output array has the correct size
    assert np.size(Hopf_netwk.update(state)) == np.size(state)
    #Test if we get an expected output for a weight matrix and state
    Hopf_netwk.weights = np.array([[0,0.33333333,-0.33333333,1.],[0.33333333,0,-1,-0.33333333],[-0.33333333,-1.,0.,-1.],[1.,-0.33333333,-1.,0.]])
    assert np.allclose(Hopf_netwk.update(state),np.array([-1, 1, 1, -1]))

def test_update_asyc():
    patterns = Generator.generate_patterns(5, 10)
    modif_state = Generator.perturb_pattern(patterns[0], 3)
    Hopf_netwk = hopfn.HopfieldNetwork(patterns)
    #Tests that the original state given to the function has maximum one of its elements that is changed
    assert (modif_state == Hopf_netwk.update_async(modif_state)).sum() >= 9

def test_dynamics():
    #Tests if the function outputs a list of correct size
    patterns = Generator.generate_patterns(40, 100)
    state = Generator.perturb_pattern(patterns[22], 10)
    #this could also have been tested following the Storkey rule (previously tested)
    Hopf_netwk = hopfn.HopfieldNetwork(patterns)
    saver = dsv.DataSaver()
    Hopf_netwk.dynamics(state, saver, 4)
    assert len(saver.get_data()["states"]) <= 4
    #Tests if the function allows the convergence towards the correct pattern if there is convergence
    saver.reset()
    Hopf_netwk.dynamics(state, saver, 20)
    last_pattern = saver.get_data()["states"][-1]
    assert Generator.pattern_match(patterns, last_pattern) == 22 or Generator.pattern_match(patterns, last_pattern) == None

def test_dynamics_async():
    #Tests if the function outputs a list of correct size
    patterns = Generator.generate_patterns(60, 1000)
    state = Generator.perturb_pattern(patterns[42], 100)
    #this could also have been tested following the Storkey rule (previously tested)
    Hopf_netwk = hopfn.HopfieldNetwork(patterns)
    saver = dsv.DataSaver()
    Hopf_netwk.dynamics_async(state, saver, 10000, 3000, 100)
    list_length = len(saver.get_data()["states"])
    assert list_length <= 100 and list_length >= 30
    #Tests if the function allows the convergence towards the correct pattern if there is convergence
    last_pattern = saver.get_data()["states"][-1]
    assert Generator.pattern_match(patterns, last_pattern) == 42 or Generator.pattern_match(patterns, last_pattern) == None
    #Test if the function stops iterating when max_iter is reached
    saver.reset()
    Hopf_netwk.dynamics_async(state, saver, 100, 101, 1)
    assert len(saver.get_data()["energies"]) == 100

def test_compute_energy():
    state = np.array([-1, 1, -1, -1])
    hebbian_matrix = np.array([[0,0.33333333,-0.33333333,1.],[0.33333333,0,-1,-0.33333333],[-0.33333333,-1.,0.,-1.],[1.,-0.33333333,-1.,0.]])
    saver = dsv.DataSaver()
    #Test if we get an expected output for a certain pattern and weights mattrix
    assert np.isclose(saver.compute_energy(state, hebbian_matrix),-2/3)

def test_random_indexer():
    assert Generator.random_indexer(1) == 0 and type(Generator.random_indexer(42)) is int

def test_chekerboard_generator():
    checkerboard = Generator.chekerboard_generator()
    for i in checkerboard:
        assert i == 1 or i == -1

def test_reset_patterns():
    Hopf_netwk = hopfn.HopfieldNetwork(Generator.generate_patterns(5,5))
    with pytest.raises(IndexError):
        Hopf_netwk.reset_patterns(7,np.ones(5))
    with pytest.raises(IndexError):
        Hopf_netwk.reset_patterns(-1,np.ones(5))
    with pytest.raises(ValueError):
        Hopf_netwk.reset_patterns(2,[1])
    with pytest.raises(ValueError):
        Hopf_netwk.reset_patterns(2,np.zeros(6))
    Hopf_netwk.reset_patterns(4,np.ones(5))
    for i in Hopf_netwk.patterns[4]:
        assert i == 1

#========================================Tests for Toolbox methods========================================

def test_sigma_function():
    assert Ut.sigma_function(-1223.90) == np.array(-1)
    assert Ut.sigma_function(526.0) == np.array(1)

def test_directory_check():
    path_to_vid = os.path.abspath('Visuals/Videos')
    path_to_gra = os.path.abspath('Visuals/Graphs')
    #test when the directory Visuals haven't been created
    test_dir_dict1 = Ut.directory_check()
    assert os.path.exists(path_to_vid) and os.path.exists(path_to_gra) and (test_dir_dict1["Videos"] == path_to_vid and test_dir_dict1["Graphs"] == path_to_gra)
    shutil.rmtree(path_to_vid)
    shutil.rmtree(path_to_gra)
    test_dir_dict2 = Ut.directory_check()
    #test when the directory Videos and Graphs haven't been created
    assert os.path.exists(path_to_vid) and os.path.exists(path_to_gra) and (test_dir_dict2["Videos"] == path_to_vid and test_dir_dict2["Graphs"] == path_to_gra)
    os.rmdir(path_to_vid)
    os.rmdir(path_to_gra)
    shutil.rmtree(os.path.abspath('Visuals'))
    #test when the directory have been created
    test_dir_dict3 = Ut.directory_check()
    assert os.path.exists(path_to_vid) and os.path.exists(path_to_gra) and (test_dir_dict3["Videos"] == path_to_vid and test_dir_dict3["Graphs"] == path_to_gra)


def test_is_decroissant():
    test_1 = [2,1,0,-2,-4,-10]
    test_2 = [10,0,-5,10,-20]
    test_3 = []
    test_4=[1]
    assert np.all([Ut.is_decroissant(test_1), not Ut.is_decroissant(test_2), Ut.is_decroissant(test_3), Ut.is_decroissant(test_4)])

def test_is_strict_decroissant():
    test_1 = [2,0,-3,-6,-10]
    test_2 = [4,2,0,-2,-2,-4]
    test_3 = [5,4,3,2,1,0,5,6]
    test_4 = []
    test_5 = [1]
    assert np.all([Ut.is_strict_decroissant(test_1), not Ut.is_strict_decroissant(test_2),
    not Ut.is_strict_decroissant(test_3),Ut.is_strict_decroissant(test_4,),Ut.is_strict_decroissant(test_5)])

#========================================Tests for Visualization methods========================================

def test_plot_energy():
    #Test if the the given list are non increasing
    rdn_patterns = Generator.generate_patterns(50, 2500)
    X = np.random.randint(0, 50)
    perturbed_pattern = Generator.perturb_pattern(rdn_patterns[X], 1000)
    saver = dsv.DataSaver()
    Hopf_netwk_hebbian = hopfn.HopfieldNetwork(rdn_patterns)
    #updates saver giving it the states and calculating their associated energy
    Hopf_netwk_hebbian.dynamics(perturbed_pattern, saver)
    #plots the energy in function of time
    saver.plot_energy('test_hebbian_Sync_plot.png')
    assert Path('test_hebbian_Sync_plot.png').is_file()
    os.remove('test_hebbian_Sync_plot.png')
    #we should destroy the object Hopf_netwk_hebbian

    # resets the object saver
    saver.reset()
    Hopf_netwk_hebbian_async = hopfn.HopfieldNetwork(rdn_patterns)
    # updates saver giving it the states and calculating their associated energy
    Hopf_netwk_hebbian_async.dynamics_async(perturbed_pattern, saver, max_iter=30000, convergence_num_iter=3000,
                                            skip=1000)
    # plots the energy in function of time
    saver.plot_energy('test_hebbian_Async_plot.png')
    assert Path('test_hebbian_Async_plot.png').is_file()
    os.remove('test_hebbian_Async_plot.png')

    #resets the object saver
    saver.reset()
    Hopf_netwk_storkey = hopfn.HopfieldNetwork(rdn_patterns, 'storkey')
    # updates saver giving it the states and calculating their associated energy
    Hopf_netwk_storkey.dynamics(perturbed_pattern, saver)
    # plots the energy in function of time
    saver.plot_energy('test_storkey_Sync_plot.png')
    assert Path('test_storkey_Sync_plot.png').is_file()
    os.remove('test_storkey_Sync_plot.png')

    # resets the object saver
    saver.reset()
    Hopf_netwk_storkey_async = hopfn.HopfieldNetwork(rdn_patterns, 'storkey')
    # updates saver giving it the states and calculating their associated energy
    Hopf_netwk_storkey_async.dynamics_async(perturbed_pattern, saver, max_iter=30000, convergence_num_iter=3000, skip=1000)
    # plots the energy in function of time
    saver.plot_energy('test_storkey_Async_plot.png')
    assert Path('test_storkey_Async_plot.png').is_file()
    os.remove('test_storkey_Async_plot.png')


def test_save_video():
    state0 = np.zeros(4)
    state1 = np.ones(4)
    # Test if the video is saved
    saver = dsv.DataSaver()
    saver.store_iter(state0)
    saver.store_iter(state1)
    saver.save_video('video.gif', img_shape=2)
    assert Path('video.gif').is_file()
    os.remove('video.gif')

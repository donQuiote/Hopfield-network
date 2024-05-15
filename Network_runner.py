import os
from Main_classes import HopfieldNetwork as hopfn
from Main_classes import DataSaver as dsv
from Main_classes import Pattern_handler as Paha

class Network_runner:
    """
    @class: Network_runner modelizes the process of the retrieving a memorized pattern starting from an unseen pattern
    @note: Two methods are in the class depending on the run wanted. A single run (general) or generating data (exp).
    """
    #the directory repertory is stored as a kwarg
    def Network_runner_general(self, pattern_numbers = 50, pattern_size = 2500, rule = 'hebbian', perturbation_numbers = 1000, update_rule = 'synchronous', video = 'off', **file_path):
        if not bool(file_path):
            raise ValueError("There is no file_path please select one from the autogenerated directories")
        else :
            print("\n\nWelcome, a Network of neurons is being created, please wait for the project to load \n")
        # Creation of a pattern handler device
        Generator = Paha.Pattern_handler()

        # Initialization of a random pattern
        rdn_patterns = Generator.generate_patterns(pattern_numbers, pattern_size)
        # Random pattern is selected and perturbed
        rd_index = Generator.random_indexer(pattern_numbers)
        perturbed_pattern = Generator.perturb_pattern(rdn_patterns[rd_index], perturbation_numbers)

        # Creation of an object type DataSaver
        saver = dsv.DataSaver()
        # Creation of an object type HopfieldNetwork
        Hopf_netwk = hopfn.HopfieldNetwork(rdn_patterns, rule = rule)

        # updates saver giving it the states and calculating their associated energy according to the update rule
        if update_rule == 'synchronous':
            Hopf_netwk.dynamics(perturbed_pattern, saver)
        elif update_rule == 'asynchronous':
            Hopf_netwk.dynamics_async(perturbed_pattern, saver, max_iter=30000, convergence_num_iter=3000,
                                                    skip=1000)
        else:
            saver.__del__()
            Hopf_netwk.__del__()
            raise ValueError("The possible update rules are only 'synchronous' or 'asynchronous'")

        # Plots the energy in function of time
        file_name = rule+'_'+update_rule
        saver.plot_energy(os.path.join(file_path["Graphs"],file_name+'_plot.png'))
        print("A graph with the", rule, update_rule, "rule has been created and stored in the Graphs directory")

        # Creates a video of the perturbed pattern returning to its original state
        if video == 'off':
            saver.__del__()
            Hopf_netwk.__del__()
            return
        elif video == 'on':
            saver.reset()
            #creates a checkerboard
            checkerboard = Generator.chekerboard_generator()

            # assigns randomly one of the pattern with the checkerboard
            # generation of a weight matrix with the checkerboard included
            Hopf_netwk.reset_patterns(rd_index, checkerboard)

            # perturb the checkerboard pattern
            perturbed_checkerboard = Generator.perturb_pattern(checkerboard, perturbation_numbers)

            # synchronous way
            if update_rule == 'synchronous':
                Hopf_netwk.dynamics(perturbed_checkerboard, saver, 20)
            elif update_rule == 'asynchronous':
                Hopf_netwk.dynamics_async(perturbed_checkerboard, saver, max_iter=30000, convergence_num_iter=3000,
                                                  skip=1000)
            saver.save_video(os.path.join(file_path["Videos"], file_name + '_video.mp4'), pattern_numbers)
            saver.__del__()
            Hopf_netwk.__del__()
            print("A video with the", update_rule,"rule has been created and stored in the Videos directory. \n\n")
        else:
            saver.__del__()
            Hopf_netwk.__del__()
            raise ValueError("Please chose whether a video of the convergence has to be created: 'on' or 'off'. \n\n")



    def Network_runner_exp(self, pattern_numbers=50, pattern_size=2500, rule='hebbian', perturbation_numbers=1000, max_iter = 100):


        # Creation of a pattern handler device
        Generator = Paha.Pattern_handler()

        # Initialization of a random pattern
        rdn_patterns = Generator.generate_patterns(pattern_numbers, pattern_size)
        # Random pattern is selected and perturbed
        rd_index = Generator.random_indexer(pattern_numbers)
        perturbed_pattern = Generator.perturb_pattern(rdn_patterns[rd_index], perturbation_numbers)

        # Creation of an object type DataSaver
        saver = dsv.DataSaver()
        # Creation of an object type HopfieldNetwork
        Hopf_netwk = hopfn.HopfieldNetwork(rdn_patterns, rule=rule)

        # updates saver giving it the states and calculating their associated energy according to the synchronous rule

        Hopf_netwk.dynamics(perturbed_pattern, saver, max_iter)
        if Generator.pattern_match(rdn_patterns, saver.get_data()["states"][-1]) == None:
            return False
        else:
            return True

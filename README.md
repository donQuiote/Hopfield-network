<h1 align="center">Hi 👋, We are team 43: Clement, Abel and Guillaume</h1>
<h3 align="center">A passionate frontend developer team from BIO-210</h3>

- 🔭 We are currently working on a **Hopfield network simulation** 🧠 with **git**.
- Here is a [summary](https://github.com/EPFL-BIO-210/BIO-210-team-43/blob/main/summary.md) of the results we obtained.
- To run the project, run in the terminal:
`python main.py`.


<h3 align="left">Project Description: </h3>

- A Hopfield network is a computational model for associative memory with a simple mechanism to explain how a neural network store representations *(i.e. the neural activity associated with a certain concept)* in the form of weighted connections between neurones.
- At any given state the network is composed of neurones that are either firing, or are not *(i.e. respectively attributed the value 1 and -1).* A state of the network can thus be understood as a pattern of 1 and -1 values.
- We will be using two different learning rules to create matrices that model the connections between neurones given a certain amounts of memory states (i.e. the *Storkey* and *Hebbian* learning rules).
- We will show that a Hopfield network with N neurones can store a certain number of network firing patterns in its synaptic weights. ⇒ If the network is presented with a pattern similar to one of the memorised patterns, the network will converge to the memorised pattern

<h3 align="left">Notes for speed tests: </h3>

*Note that the cythonized versions are only available on the branch numba_test*

- We tried to cythonize all of our functions but we finally only kept the cythonized versions of
hebbian_weights, storkey_weights, perturb_pattern and generate_patterns.
- **Timeit** provides a way to measure the execution time of the different functions. It works as follow: Each important function and its associated cythonized function have their timer functions. The time are constructed in such a way that the measurements are much more precise than just saving the time before and after the function execution. The function sums 100 runs, this is done 5 times, then the minimum value is taken giving a lower bound for how fast the machine can run the given code snippet. *This is the best way to do given that higher values are typically not caused by variability in Phyton's speed but more by other processes in the machine.*
- We have implemented cython, however all of the function in numpy are already faster (written C). Thus please *test only the speed of the functions only in Hopfield.py, Utilities.py and Visualization.py*

<h3 align="left">Installations: </h3>

The req.txt file can be run to automatically create an environement with the needed installations to run the code.

 `conda create --name <env> --file req.txt`.

 The previous file was made with PyCharm IDE. 

- **pytest** : Package used for testing in the *test_Hopfield_network* module.
- **coverage** : Package used to check the lines of code that are tested thanks to the tests from the *test_Hopfield_network* module.
- 🅽 **numpy** : Package used for its ndarrays and its integrated math functions that bring considerable velocity to our code.
- 📉 **mathplotlib** : Package used for plotting the graphs and videos to visualise the evolution of our Hopfield network.
- 🎲 **random** : Package used for generating random output.
- **cython** : Run python *setup.py build_ext --inplace* (builds the cython file), followed by *cython -a update_cython.pyx firefox update_cython.html* (to vizualise the lines of code that were cythonized with firefox). This implementation speeds the code only for certain functions (the cythonized versions of
hebbina_weights, storkey_weights, perturb_pattern and generate_patterns are will be used).
- 🪑 **benchmark** : Package to test the speed of funtions for several iterations and by comparing their velocity.
- 👤 **cProfile** : Package to profile the execution of our main function from main.py. This gives incite on how to do further optimisations of our code.
- ⏳ **timeit** : Package to time of execution of functions. This package is used extensively in the timer.py file.
- 🐼 **pandas** : Package that allows the manipulation and the analysis of data.
- **tabulate** : Package that offers a nice format when printing a table.
- **pytables** : Package to manage hierarchical datasets of very big size.


<h3 align="left">Main files: </h3>

- 🌐 **HopfieldNetwork.py** : Defines the class that will modelise our Hopfield network from a set of patterns and a given learning rule.
- 🛠 **Utilities.py** : Stores the functions of general use used throughout the project.
- 👁 **DataSaver.py** : DataSaver is used to save the data generated during the process of convergence of a perturbed state (pattern) to a state belonging to the set of patterns of a HopfieldNetwork. It also  disposes of methods that help to visualise the progress in the Hopfield network *(e.g. how quickly a pattern is recognised by analogy to a memorised pattern)*.
- 🏃‍♂️**Network_runner** : The function in this file enables to modularise the code that is run in the main file.
- 🖖 **Pattern_handler** : This class can generate patterns of a given size and can disrupt them. It acts as a smooth interface to manipulate the patterns throughout this project.
- 🏡 **main.py** : This is the file from which one runs the simulations and tests the convergence of a pattern similar to a previously encountered one. It is composed of a main function that makes several calls to a Network_runner and experiment.
- 🧪 **test_Hopfield_network.py** : Takes care of testing the methods of this project. It uses pytest and doctests for unit testing.
- **cProfiler.py** : File needed to generate the profiling of the main function in main.py *(c.f. informations above concerning the cProlfile package)*.
- ⏱ **timer.py** : Contains functions that individually computes the runtime of a corresponding function for the project. It is used to compare different versions of a given function *(e.g. comparing of the cythonized version of a function with the python version)*.


<h3 align="left">Languages and Tools: Python using numpy, matplotlib, coverage and pytest amoung others</h3>
<p align="left">  </a> <a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>

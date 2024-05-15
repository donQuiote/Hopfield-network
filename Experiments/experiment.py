from math import sqrt, log
import numpy as np
import Network_runner as rn
import pandas as pd
import os.path
from Experiments import Experiment_Graph_Generator as egg
from Main_classes import Utilities as ut

sizes = [10, 18, 34, 63, 116, 215, 397, 733, 1354, 2500]
rules = ['hebbian', 'storkey']



def experiment_handler(number_of_t = 10 , rate_of_perturbation = 1.0/5.0, **file_path):
    results = []
    graph_gen = egg.GraphGenerator()

    for rule in rules:
        for i in sizes:
            list_t = []
            list_frac = []
            for t in range (number_of_t):
                t = t_generator(i, rule)
                list_t.append(t)
                exp = experiment(i, t, rule, int(rate_of_perturbation*i))
                list_frac.append(exp["match_frac"])
                results.append(exp)

            graph_gen.general_graph(list_t, list_frac, file_path["Capacity_Graphs"], rule, i)

    #final graphs
    graph_gen.summary_graph(results,sizes, file_path["Capacity_Graphs"])
    result_table_generator(results, os.path.join(file_path["Capacity_Graphs"], 'capacity.hdf5'))


def experiment(size, num_patterns, weight_rule, num_perturb, num_trials=10, max_iter=100):
    Runner = rn.Network_runner()
    match = 0
    for i in range (num_trials):
        if Runner.Network_runner_exp(num_patterns, size, weight_rule, num_perturb, max_iter):
            match += 1

    match_frac = match/num_trials
    results_dict = {
        "network_size": size,
        "weight_rule": weight_rule,
        "num perturb": num_perturb,
        "match_frac": match_frac,
        "num_patterns": num_patterns
    }
    return results_dict


def t_generator(size, weight_rule):
    toolbox = ut.Utilities()
    if weight_rule == 'hebbian':
        return np.random.choice(np.linspace(0.5*toolbox.C_heb(size), 2*toolbox.C_heb(size), 10).astype(int))
    else:
        return np.random.choice(np.linspace(0.5*toolbox.C_sto(size), 2*toolbox.C_sto(size), 10).astype(int))


def result_table_generator(results, out_path):
    # Create a pandas DataFrame from results dictionary
    df = pd.DataFrame(results)
    print (df)
    # Save dataframe as an hdf5 file
    df.to_hdf(out_path, key='df')
    # Additionally you can let pandas print the table in markdown format for easy pasting!
    print(df.to_markdown())


def exp_robustness(t=2, **file_path):

    graph_gen = egg.GraphGenerator()
    results = []
    perturbs = np.arange(0, 1, 0.05)

    for rule in rules:
        for i in sizes:
            list_frac = []
            list_perturbation_number = []
            for j in perturbs:
                perturbation_number = int(i*j)
                list_perturbation_number.append(perturbation_number)
                robust_exp = experiment(i,t,rule, perturbation_number)
                list_frac.append(robust_exp['match_frac'])
                results.append(robust_exp)

            graph_gen.general_graph(list_perturbation_number, list_frac, file_path["Robustness_Graphs"],rule, i,'robust')

    result_table_generator(results, os.path.join(file_path["Robustness_Graphs"], 'robustness.hdf5'))

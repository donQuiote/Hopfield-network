import matplotlib.pyplot as plt
import os
import numpy as np
from Main_classes import Utilities as ut


class GraphGenerator:
    """
    @class: GraphGenerator is used to create and save graph from different kind of experiment.
    """

    def out_path_generator(self, rule, size_network, directory_name, graph_type):
        if graph_type == 'summary':
            return os.path.join(directory_name,f'{rule}_summary_graph.png')
        if graph_type == 'regular':
            return os.path.join(directory_name,f'{rule}_of_size_{str(size_network)}.png')
        if graph_type == 'robust':
            return os.path.join(directory_name, f'{rule}_robustness_of_size_{str(size_network)}.png')

    def general_graph(self, list_X, list_Y, directory_path, rule, size_network = None, graph_type = 'regular'):
        out_path = self.out_path_generator(rule, size_network, directory_path, graph_type)
        plt.figure(figsize=(10, 6), dpi=130)

        if graph_type == 'regular':
            axis_x = "Number of patterns"
            axis_y = "Fraction of retrieved patterns"
            legend = f'Capacity plot for n={size_network} with {rule} rule'
        elif graph_type == 'summary':
            axis_x = "Network"
            axis_y = "Capacity"
            legend = f'Summary of network capacity plot with {rule} rule'
            legend_th = f'Theoretical network capacity with {rule} rule'
            toolbox = ut.Utilities()
            if rule == 'hebbian':
                C_plot = toolbox.C_heb(list_X)
            elif rule == 'storkey':
                C_plot = toolbox.C_sto(list_X)
            plt.plot(list_X,C_plot, 'b-', label = legend_th)

        elif graph_type == 'robust' :
            axis_x = "Number of perturbations"
            axis_y = "Fraction of retrieved patterns"
            legend = f'Robustness plot for n={size_network} with {rule} rule'
        else :
            raise NameError("Please select a correct graph_type between 'regular', 'summary' or 'robust'")

        title = out_path
        index = out_path.find('hebbian')
        if index != -1:
            title = out_path[index:]
        index = out_path.find('storkey')
        if index != -1:
            title = out_path[index:]
        plt.title(title.replace(".png", ''), fontdict={'fontsize': 25})
        plt.plot(list_X, list_Y, 'r.', markersize=10, label = legend)
        plt.legend()
        plt.xlabel(axis_x)
        plt.ylabel(axis_y)

        #saving the figure
        plt.savefig(out_path)

    def summary_graph (self, results, sizes, file_path):
        """
        @note: heavier code to read but is faster to go through the dictionaries
        """
        max_number_of_t_HEB = []
        max_number_of_t_STO = []
        for i in sizes:
            biggest_number_of_t_HEB = 0
            biggest_number_of_t_STO = 0
            for dico in results:
                if dico["network_size"] == i and dico["match_frac"] >= 0.9:
                    if dico["weight_rule"] == 'hebbian':
                        pattern_size = dico["num_patterns"]
                        if (biggest_number_of_t_HEB < pattern_size):
                            biggest_number_of_t_HEB = pattern_size
                    if dico["weight_rule"] == 'storkey':
                        pattern_size = dico["num_patterns"]
                        if (biggest_number_of_t_STO < pattern_size):
                            biggest_number_of_t_STO = pattern_size
            max_number_of_t_HEB.append(biggest_number_of_t_HEB)
            max_number_of_t_STO.append(biggest_number_of_t_STO)
        self.general_graph(sizes, max_number_of_t_HEB, directory_path=file_path, rule= 'hebbian', graph_type='summary')
        self.general_graph(sizes, max_number_of_t_STO, directory_path=file_path, rule= 'storkey', graph_type='summary')

            

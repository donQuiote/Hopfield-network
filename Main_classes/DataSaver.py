import numpy as np
import matplotlib.animation as anim
import matplotlib.pyplot as plt
from math import sqrt


class DataSaver:
    """
    @class: DataSaver is used to save the data generated during the process of convergence of a state (pattern)
        to a state belonging to the set of patterns of a HopfieldNetwork.
    """

    def __init__(self):
        """
        @note: One attriute is given to the DataSaver object upon initialization, namely data
            data will store the states and their associated energies with store_iter that is called dynamic methods of a HopfieldNetwork
        """
        self.data = {"states": [], "energies": []}

    def reset(self):
        self.data = {"states": [], "energies": []}

    def store_iter(self, state = None, weights = None):
        """
        @summary: store_iter will be called in dynamic functions of a HopfieldNetwork to store selected states and their associated energies
        @param state: the current state of the pattern during the process of convergence in a dynamics method
        @param weights: the weights of the HopfieldNetwork which runs the dynamic method in which store_iter is called
        """
        if state is not None:
            self.data["states"].append(state.copy())
        if weights is not None:
            self.data["energies"].append(self.compute_energy(state, weights))

    def compute_energy(self, state, weights):
        """
        @summary: energy gives the energy at a specific time given the weight matrix and a state
        @param state: A pattern in the form of an array.
        @param weights: a matrix (array of array) of same random size as state
        @return: the energy of the weight matrix proportional to a given pattern (double)
        """
        return np.sum(weights * np.outer(state,state))*(-0.5)

    def get_data(self):
        return self.data

    def save_video(self, out_path = "Untitled.gif", img_shape = 50, img2_shape = [6.4, 4.8]):
        """
        @summary: save_video creates an animation of a the list received.
                This list contains multiple arrays, each one of them is a converted into a frame.
                Afterwards, it stores the video into the file it's being used under the name out_path received.
        @param self: a dictionnary linking each weight matrix to it's corresponding energybe converted in the animation.
        @param out_path: The name of the file (format gif) where the animation is saved.
        @param img_shape: the size
        @note: Create a animation video of the network state converging to a memorized pattern.
        """
        #setup
        writer = anim.FFMpegWriter(fps=3,metadata=dict(artist='Me'),bitrate=2000)
        fig = plt.figure(figsize=(img2_shape[0], img2_shape[1]), dpi=130)
        frames = []

        #transforms 1D state into 2D image
        #shape = int(sqrt(len(self.data["states"][0])))
        for i in range(len(self.data["states"])):
            frames.append([plt.imshow(np.reshape(self.data["states"][i], (img_shape,img_shape)), cmap = 'gray')])
        animation = anim.ArtistAnimation(fig,frames)

        animation.save(out_path)

    def plot_energy(self, out_path = "Untitled.png"):
        """
        @summary: save_video plots the energy of a state at each step creating a graph
                of the energy of a matrix in function of time.
        @param out_path: The path where the image is going to be stored, and especially it's name and the name of the graph
        @show : opens a window containing a double plot, the top subplot titles Hebbian and the lower one title's Storkey
        """
        axis_x = "Time [step]"
        axis_y = "Energy"
        legend = 'Energy at each Step'
        plt.figure(figsize=(10, 6),dpi=130)
        plt.plot(self.data["energies"],color='r', marker= '.',linewidth=2,linestyle= '--', markersize = 15, label = legend, markeredgecolor= 'black')
        plt.xlabel(axis_x)
        plt.ylabel(axis_y)
        plt.xticks(range(len(self.data["states"])))
        title = out_path
        index = out_path.find('hebbian')
        if (index != -1):
            title = out_path[index:]
        index = out_path.find('storkey')
        if (index != -1):
            title = out_path[index:]
        plt.title(title.replace(".png",''), fontdict = {'fontsize': 25})
        plt.legend()
        for i, v in enumerate(self.data["energies"]):
            plt.text(i, v - v/10, "%d" % v, ha="center")
        plt.savefig(out_path)
        plt.show()

    def __del__(self):
        self.reset()
        del self




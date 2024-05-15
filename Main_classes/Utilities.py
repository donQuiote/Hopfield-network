import os
import numpy as np

class Utilities:
     """
     @class: Utilities stores various useful methods used in HopfieldNetwork methods and for unit testing amoung others
     """

     def C_heb(self, n):
         return n / (2 * np.log(n))

     def C_sto(self, n) :
         return n / np.sqrt(2 * np.log(n))

     def sigma_function(self, x) :
         '''
         @summary: sigma function takes a random input and returns 1 if the input is bigger or equal to 0 and
                -1 if the value is smaller than 0
         @param x: the input of any type
         @examples:
         >>> sigma_function(87.3)
         array(1)
         >>> sigma_function(-1223.90)
         array(-1)
         '''
         return np.where(x >= 0, 1, -1)

     def directory_check(self):
        """
        @summary: directory_check checks whether the directories in which the graphs and videos are going to be stored
            exists and are correctly setup
        @return: a dictionary with the path to the Videos directory and the Graphs directory, Images directory and Exp_dt directory
        """
        path_to_vis = os.path.abspath('Visuals')
        path_to_vid = os.path.join(path_to_vis, 'Videos')
        path_to_gra = os.path.join(path_to_vis, 'Graphs')
        path_to_ima = os.path.join(path_to_vis, 'Images')
        path_to_exp = os.path.join(path_to_vis, 'Exp_Data')
        path_to_robu = os.path.join(path_to_exp, 'Robustness_Graphs')
        path_to_capa = os.path.join(path_to_exp, 'Capacity_Graphs')
        if not (os.path.isdir(path_to_vis)):
            self.directory_creator(path_to_vis)
            self.directory_creator(path_to_vid)
            self.directory_creator(path_to_gra)
            self.directory_creator(path_to_ima)
            self.directory_creator(path_to_exp)
            self.directory_creator(path_to_robu)
            self.directory_creator(path_to_capa)
        if not (os.path.isdir(path_to_vid)):
            self.directory_creator(path_to_vid)
        if not (os.path.isdir(path_to_gra)):
            self.directory_creator(path_to_gra)
        if not (os.path.isdir(path_to_ima)):
            self.directory_creator(path_to_ima)
        if not (os.path.isdir(path_to_exp)):
            self.directory_creator(path_to_exp)
            self.directory_creator(path_to_robu)
            self.directory_creator(path_to_capa)
        if not (os.path.isdir(path_to_capa)):
            self.directory_creator(path_to_capa)
        if not (os.path.isdir(path_to_robu)):
            self.directory_creator(path_to_robu)
        else:
            print("Directory is correctly setup ")
        print(path_to_capa)
        return({"Videos" : path_to_vid, "Graphs" : path_to_gra, "Images" : path_to_ima, "Exp_Data" : path_to_exp,
                'Robustness_Graphs' : path_to_robu, 'Capacity_Graphs' : path_to_capa })

     def directory_creator(self, path):
        os.mkdir(path)
        print(path[path.rfind('/')+1:], "directory created")

     def is_decroissant(self,lst):
        for i in range(len(lst)-1):
            if not lst[i] >= lst[i+1]:
                return False
        return True

     def is_strict_decroissant(self,lst):
        for i in range(len(lst)-1):
            if not lst[i] > lst[i+1]:
                return False
        return True

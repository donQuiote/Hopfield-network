from Main_classes import Utilities as ut
from timeit import default_timer as timer
import Network_runner as rnr
from Experiments import experiment as xp
from Recalling_Images.image_finder import image_finder
from Recalling_Images.image_reformer import image_reformer

def main():
    start = timer()

    #Creation of objects
    runner = rnr.Network_runner()
    toolbox = ut.Utilities()

    # directory update:
    dir_dict = toolbox.directory_check()

    #number of t generated by default is 10 and rate of perturbation by default is 1 / 5
    xp.experiment_handler(**dir_dict)

    #number of patterns is by default 2
    xp.exp_robustness(**dir_dict)

    #A thick yoshi is used by default
    converted_image = image_reformer()

    image_finder(image = converted_image, **dir_dict)

    #Hebbian synch way and video
    runner.Network_runner_general( video = 'on', **dir_dict)

    #Hebbian asynch way and video
    runner.Network_runner_general(update_rule = 'asynchronous', video = 'on', **dir_dict)

    #Storkey synch way
    runner.Network_runner_general(rule = 'storkey' , video='off', **dir_dict)

    #Storkey asynch way
    runner.Network_runner_general(rule = 'storkey', update_rule = 'asynchronous', video='off', **dir_dict)

    print(timer()-start)

if __name__ == '__main__':
    main()

"""
Run decision tree

Usage:
    dt_run.py <pre_name> <max_height> <min_size> 

Examples:
    dt_run.py c45/vote 5 10 

Arguments:
    pre_name            dataset name based on path /mnt/recdata/personal/chunyang/dataset/
    max_height          The maximum height of the tree 
    min_size            The minimum size of the tree when stop building

Options:
    -h, --help
"""
import sys
import time
from docopt import docopt

from dt_model import *
from split_method import *
from dt_trainer import *
from dt_predictor import *

if __name__=='__main__':
    args = docopt(__doc__, version='1.0.0')
    pre_name = args['<pre_name>'] 
    max_height = int(args['<max_height>'])
    min_size = int(args['<min_size>'])
    trainer = DT_Trainer(max_height, min_size, EntropySplitMethod())
    start = time.time()
    data_path = "/mnt/recdata/personal/chunyang/dataset/"
    trainer.load_feature_list(data_path + pre_name + ".feature")
    trainer.load_dataset(data_path + pre_name + ".data.dt")
    elapsed = time.time() - start
    print "Loading time:", elapsed

    start = time.time()
    trainer.train()
    elapsed = time.time() - start
    print "Training time:", elapsed
    trainer.model.save_model(data_path + pre_name + ".model_" + str(max_height) + "_" + str(min_size))
    
    start = time.time()
    predictor = DT_Predictor(trainer.model)
    predictor.load_dataset(data_path + pre_name + ".test.dt")
    predictor.predict(data_path + pre_name + ".score_test_" + str(max_height) + "_" + str(min_size))
    elapsed = time.time() - start
    print "Testing time:", elapsed
    
    predictor2 = DT_Predictor(trainer.model)
    predictor2.load_dataset(data_path + pre_name + ".data.dt")
    predictor2.predict(data_path + pre_name + ".score_train_" + str(max_height) + "_" + str(min_size))

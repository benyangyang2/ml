"""
Run Random Forest

Usage:
    rf_run.py <pre_name> <max_height> <min_size> <tree_cnt> <fea_cnt> 

Examples:
    rf_run.py c45/vote 5 10 100 5 

Arguments:
    pre_name            dataset name based on path /mnt/recdata/personal/chunyang/dataset/
    max_height          The maximum height of the tree 
    min_size            The minimum size of the tree when stop building
    tree_cnt            Tree counts in the forest
    fea_cnt             Feature count for each tree

Options:
    -h, --help
"""
import sys
import time
from docopt import docopt

from dt_model import *
from split_method import *
from rf_trainer import *
from dt_predictor import *
from rf_predictor import *

if __name__=='__main__':
    args = docopt(__doc__, version='1.0.0')
    pre_name = args['<pre_name>'] 
    max_height = int(args['<max_height>'])
    min_size = int(args['<min_size>'])
    tree_cnt = int(args['<tree_cnt>'])
    fea_cnt = int(args['<fea_cnt>'])
    trainer = RF_Trainer(max_height, min_size, EntropySplitMethod(), tree_cnt, fea_cnt)
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
    #trainer.model.save_model(data_path + pre_name + ".model_" + str(max_height) + "_" + str(min_size))
    
    start = time.time()
    predictor = RF_Predictor(trainer.model)
    predictor.load_dataset(data_path + pre_name + ".test.dt")
    predictor.predict(data_path + pre_name + ".score_test_rf_" + str(max_height) + "_" + str(min_size) + "_" + str(tree_cnt) + "_" + str(fea_cnt))
    elapsed = time.time() - start
    print "Testing time:", elapsed
    
    predictor2 = DT_Predictor(trainer.model)
    predictor2.load_dataset(data_path + pre_name + ".data.dt")
    predictor2.predict(data_path + pre_name + ".score_train_rf_" + str(max_height) + "_" + str(min_size))

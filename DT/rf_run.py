import sys
import time
from model import *
from split_method import *
from rf_trainer import *
from predictor import *
from rf_predictor import *

if __name__=='__main__':
    pre_name = sys.argv[1]
    max_height = int(sys.argv[2])
    min_size = int(sys.argv[3])
    tree_cnt = int(sys.argv[4])
    fea_cnt = int(sys.argv[5])
    trainer = RF_Trainer(max_height, min_size, EntropySplitMethod(), tree_cnt, fea_cnt)
    start = time.time()
    data_path = "/mnt/recdata/momData/dataset/syw/"
    trainer.load_feature_list(data_path + pre_name + ".feature")
    trainer.load_dataset(data_path + pre_name + ".data.dt")
    #trainer.load_dataset("/mnt/recdata/momData/dataset/syw/samples_train.txt")          
    #trainer.load_feature_list("/mnt/recdata/momData/dataset/syw/feature.txt")
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

import sys
import time
from dt_model import *
from split_method import *
from dt_trainer import *
from dt_predictor import *

if __name__=='__main__':
    pre_name = sys.argv[1]
    max_height = int(sys.argv[2])
    min_size = int(sys.argv[3])
    trainer = DT_Trainer(max_height, min_size, EntropySplitMethod())
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

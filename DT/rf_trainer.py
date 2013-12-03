import sys
from dt_model import *
from tree_node import *
from sample import *
from dt_model import *
from rf_model import *
from dt_trainer import *
from split_method import *
from random import * 

class RF_Trainer:
    def __init__(self, max_height, min_tree_size, split_method, tree_cnt, fea_cnt):
        self.max_height = max_height
        self.min_tree_size = min_tree_size
        self.split_method = split_method
        self.tree_cnt = tree_cnt
        self.fea_cnt = fea_cnt
        self.dataset = []
        self.model = RF_Model()
        self.features = {}

    def load_dataset(self, data_path):
        for line in open(data_path):
            sample = DT_Sample(line)
            #sample = BinarySample(line, self.model.features)
            self.dataset.append(sample)
        print "Finish load dataset, size is:", len(self.dataset)

    def load_feature_list(self, data_path):
        for line in open(data_path):
            feature = Feature(line)
            self.features[feature.id] = feature
        #self.model.load_feature(data_path)
        print "Finish load feature, size is:", len(self.features)

    def train(self):
        data_size = len(self.dataset)
        for i in xrange(self.tree_cnt):
            print "Start building tree:", i
            # Generate random dataset
            random_dataset = []
            for j in xrange(data_size):
                r = randint(0, data_size - 1)
                random_dataset.append(self.dataset[r])
            # Generate random feature_list
            random_feature_list = {}
            r_fids = sample(self.features.keys(), self.fea_cnt) 
            for fid in r_fids:
                random_feature_list[fid] = self.features[fid]

            dt_trainer = DT_Trainer(self.max_height, self.min_tree_size, EntropySplitMethod())
            dt_trainer.set_dataset(random_dataset)
            dt_trainer.set_feature_list(random_feature_list)
            dt_trainer.train()

            self.model.add_dt_model(dt_trainer.model)

if __name__=='__main__':
    trainer = DT_Trainer(20, 10, GiniSplitMethod())
    trainer.load_dataset("/mnt/recdata/momData/dataset/syw/samples_train_10w.txt")          
    trainer.load_feature_list("/mnt/recdata/momData/dataset/syw/feature.txt")
    trainer.train()
    trainer.model.save_model("model1.txt")

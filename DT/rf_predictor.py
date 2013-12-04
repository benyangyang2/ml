import sys
from dt_model import *
from tree_node import *
from sample import *
from dt_model import *
from split_method import *

class RF_Predictor:
    def __init__(self, model): 
        self.dataset = []
        self.model = model

    def load_dataset(self, data_path):
        for line in open(data_path):
            #sample = BinarySample(line, self.model.features)
            sample = DT_Sample(line, len(self.model.features))
            self.dataset.append(sample)
        print "Finish load dataset, size is:", len(self.dataset)

    def load_feature_list(self, data_path):
        self.model.load_feature(data_path)
        print "Finish load feature, size is:", len(self.model.features)
        print self.model.features

    def predict(self, out_file):
        f_out = open(out_file, "w")
        for sample in self.dataset:
            label = "1" if sample.label else "0"
            print >>f_out, label, self.model.predict(sample)


import sys
from model import *
from tree_node import *
from sample import *
from model import *

class DT_Trainer:
    def __init__(self, max_height, min_tree_size, split_method):
        self.max_height = max_height
        self.min_tree_size = min_tree_size
        self.dataset = []
        self.model = DT_Model()

    def load_dataset(self, data_path):
        for line in open(data_path):
            sample = DT_Sample(line)
            self.dataset.append(sample)

    def load_feature_list(self, data_path):
        self.model.load_feature(data_path)

    def train(self, dataset):
        self.model.root = self.build_tree(dataset)

    def build_tree(self, dataset, visited_feature, height):
        
       


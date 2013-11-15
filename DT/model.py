from tree_node import *
from feature import *

class DT_Model:
    def __init__(self):
        self.root = None 
        self.features = {}

    def load_feature(self, data_path):
        for line in open(data_path):
            feature = Feature(line)
            self.features[feature.id] = feature

    def load_model(self):
        return
    
    def save_model(self, data_path):
        f_model = open(data_path)
        save_tree(self.root, 0, f_model)

    def save_tree(self, root, height, f_model):
        if root.is_leaf:
            print >>f_model, "".join(["\t"] * height), self.data_count, self.prob 
            return
        print >>f_model, "".join(["\t"] * height), self.data_count, self,split_feature, self.split_feature_threshold 
        
        for sub in self.children:
            self.save_tree(sub, height + 1, f_model)

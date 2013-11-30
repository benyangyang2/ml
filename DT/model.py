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
        f_model = open(data_path, "w")
        self.save_tree(self.root, 0, f_model)

    def save_tree(self, root, height, f_model):
        if root.is_leaf:
            print >>f_model, "".join([" "] * height), root.data_count, root.prob 
            return
        print >>f_model, "".join([" "] * height), root.data_count, root.split_feature.id, \
                root.split_feature_threshold 
        print >>f_model, "(", root.split_value_2_index, ")"
        
        for sub in root.children:
            self.save_tree(sub, height + 1, f_model)

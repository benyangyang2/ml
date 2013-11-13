from tree_node import *
from feature import *

class DT_Model:
    def __init__(self):
        self.root = TreeNode()
        self.features = {}

    def load_feature(self, data_path):
        for line in open(data_path):
            feature = Feature(line)
            self.features[feature.id] = feature

    def load_model(self):
        return
    
    def save_model(self):
        return

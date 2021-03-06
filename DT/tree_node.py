from feature import *
class TreeNode:
   def __init__(self, is_leaf):
       pass

class LeafNode(TreeNode):
    def __init__(self, data_count, positive_count):
        self.is_leaf = True
        self.data_count = data_count
        self.positive_count = positive_count
        self.prob = float(positive_count) / data_count
        
class MiddleNode(TreeNode):
    def __init__(self, data_count, positive_count, split_feature, threshold = None):
        self.is_leaf = False
        self.data_count = data_count
        self.positive_count = positive_count
        self.prob = float(positive_count) / data_count
        self.split_feature = split_feature
        self.split_feature_threshold = threshold
        self.children = []
        self.split_value_2_index = {}
        
    def add_child(self, child, split_value):
        self.split_value_2_index[split_value] = len(self.children) 
        self.children.append(child)

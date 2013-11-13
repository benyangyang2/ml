from feature_type import *
class TreeNode:
   def __init__(self):
       self.children = []
       self.is_leaf = True
       self.split_feature_index = None
       self.split_feature_type = FeatureType.DISCRETE 
       self.split_feature_threshold = None
       self.data_count = 0
       self.positive_count = 0

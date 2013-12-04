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
    
    def predict(self, sample):
        return self.predict_recur(sample, self.root)

    def predict_recur(self, sample, root):
        if root.is_leaf:
            return root.prob
        split_feature = root.split_feature
        #sample_feature_value = sample.features.get(split_feature.id, "0")
        sample_feature_value = sample.features[split_feature.id]
        if split_feature.type == FeatureType.DISCRETE:
            if not sample_feature_value in root.split_value_2_index:
                return root.prob
            i = root.split_value_2_index[sample_feature_value]
            return self.predict_recur(sample, root.children[i])
        else:
            if float(sample_feature_value) <= float(root.split_feature_threshold):
                return self.predict_recur(sample, root.children[0])
            else:
                return self.predict_recur(sample, root.children[1])

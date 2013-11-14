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
        self.split_method = split_method

    def load_dataset(self, data_path):
        for line in open(data_path):
            sample = DT_Sample(line)
            self.dataset.append(sample)

    def load_feature_list(self, data_path):
        self.model.load_feature(data_path)

    def train(self, dataset):
        self.model.root = self.build_tree(dataset)

    def build_tree(self, dataset, visited_feature_ids, height):
        data_count = len(dataset)
        pos_count = get_pos_count(dataset)
        if data_count <= self.min_tree_size || height >= self.max_height \
            || pos_count == data_count || pos_count == 0:
            return LeafNode(data_count, pos_count)
            
        dt_pure = self.split_method.calc_pure(dataset)
        max_gain = 0
        best_feature = None
        best_threshold = None
        for feature in self.model.features:
            if feature.id in visited_feature_ids:
                continue
            gain, threshold = self.split_method.get_max_pure_gain(dataset, feature, dt_pure)
            if gain > max_gain:
                max_gain = gain
                best_feature = feature
                best_threshold = threshold
        if max_gain == 0:
            return LeafNode(data_count, pos_count)
        if feature.type == FeatureType.DISCRETE:
            visited_feature_ids.append(best_feature.id)
        root = MiddleNode(data_count, best_feature, best_threshold)
        splited_datasets = self.split_dataset(dataset, best_feature, best_threshold)
        for sub_dt in splited_datasets:
            root.add_child(self.build_tree(sub_dt, visited_feature_ids, height + 1)
        return root
    
    def split_dataset(self, dataset, feature, threshold):
        if feature.type == FeatureType.DISCRETE:
            new_datasets = {}
            for sample in dataset:
                f_value = sample.features[feature.id]
                dt = new_datasets.get(f_value, [])
                dt.append(sample)
                new_datasets[f_value] = dt
        else:
            new_datasets = [[], []]
            for sample in dataset:
                f_value = sample.features[feature.id]
                if f_value <= threshold:
                    new_datasets[0].append(sample)
                else:
                    new_datasets[1].append(sample)
        return new_datasets.values()
                 
            
       


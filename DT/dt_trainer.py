import sys
from dt_model import *
from tree_node import *
from sample import *
from dt_model import *
from split_method import *

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
            #sample = BinarySample(line, self.model.features)
            self.dataset.append(sample)
        print "Finish load dataset, size is:", len(self.dataset)

    def set_dataset(self, dataset):
        self.dataset = dataset

    def load_feature_list(self, data_path):
        self.model.load_feature(data_path)
        print "Finish load feature, size is:", len(self.model.features)

    def set_feature_list(self, feature_list):
        self.model.features = feature_list

    def train(self):
        self.model.root = self.build_tree(self.dataset, [], 0)

    def build_tree(self, dataset, visited_feature_ids, height):
        data_count = len(dataset)
        pos_count = get_pos_count(dataset)
        if data_count <= self.min_tree_size or height >= self.max_height \
            or pos_count == data_count or pos_count == 0:
            return LeafNode(data_count, pos_count)
            
        dt_pure = self.split_method.calc_pure(dataset)
        max_gain = 0
        best_feature = None
        best_threshold = None
        for f_id in self.model.features.keys():
            feature = self.model.features[f_id]
            if f_id in visited_feature_ids:
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
        root = MiddleNode(data_count, pos_count, best_feature, best_threshold)
        #print "------------Build middle node:", max_gain, height, best_feature.id, best_threshold, data_count
        splited_datasets = self.split_dataset(dataset, best_feature, best_threshold)
        for feature_value in splited_datasets.keys():
            sub_dt = splited_datasets[feature_value]
            root.add_child(self.build_tree(sub_dt, visited_feature_ids, height + 1), feature_value)
        return root
    
    def split_dataset(self, dataset, feature, threshold):
        if feature.type == FeatureType.DISCRETE:
            new_datasets = {}
            for sample in dataset:
                #f_value = sample.features[feature.id]
                f_value = sample.features.get(feature.id, "0")
                dt = new_datasets.get(f_value, [])
                dt.append(sample)
                new_datasets[f_value] = dt
            return new_datasets
        else:
            new_datasets = {0: [], 1:[]}
            for sample in dataset:
                f_value = sample.features[feature.id]
                if float(f_value) <= float(threshold):
                    new_datasets[0].append(sample)
                else:
                    new_datasets[1].append(sample)
            return new_datasets

if __name__=='__main__':
    trainer = DT_Trainer(20, 10, GiniSplitMethod())
    trainer.load_dataset("/mnt/recdata/momData/dataset/syw/samples_train_10w.txt")          
    trainer.load_feature_list("/mnt/recdata/momData/dataset/syw/feature.txt")
    trainer.train()
    trainer.model.save_model("model1.txt")

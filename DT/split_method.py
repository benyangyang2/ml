from sample import *
from feature_type import *
class SplitMethod:
    def __init__(self):
        pass
    def get_max_pure_gain(self, dataset, dt_pure):
        raise NotImplementedError('SplitMethod.get_max_pure_gain is an abstract function')
    def calc_pure(self, dataset):
        raise NotImplementedError('SplitMethod.calc_pure is an abstract function')

class GiniSplitMethod(SplitMethod):
    def get_max_pure_gain(self, dataset, feature, dt_pure):
        if feature.type == FeatureType.DISCRETE:
            current_pure = 0
            dt_len = len(dataset)
            total_count = {}
            pos_count = {}
            f_id = feature.id
            for value in feature.values:
                total_count[value] = 0
                pos_count[value] = 0
            for sample in dataset:
                f_value = sample.features[f_id]
                total_count[f_value] += 1
                if sample.label is True:
                    pos_count += 1
            for value in feature.values:
                p = float(pos_count[value]) / total_count[value]
                current_pure += float(total_count[value]) / dt_len* (2 * p - 2 * p * p)
            return dt_pure - current_pure, None

        elif feature_type == FeatureType.CONTINUAL:
            f_id = feature.id
            sorted_dt = sorted(dataset, key=lambda sample:sample.features[f_id])
            total_count = len(dataset)
            total_pos_count = 0
            for sample in sorted_dt:
                if sample.label is True:
                    total_pos_count += 1

            threshold = None
            max_gain = 0
            former_count = 0
            former_pos_count = 0
            for i in xrange(len(sorted_dt) - 1):
                sample = sorted_dt[i]
                former_count += 1
                if sample.label is True:
                    former_pos_count += 1
                if sample.features[f_id] == sorted_dt[i+1].features[f_id]:
                    continue
                former_p = float(former_pos_count) / former_count
                latter_p = float(total_pos_count - former_pos_count) / (total_count - former_count)
                current_pure = float(former_count)/total_count * (2 * former_p - 2 * former_p * former_p) \
                    + float(total_count - former_count)/total_count * (2 * latter_p - 2 * latter_p * latter_p)
                
                gain = dt_pure - current_pure
                if gain > max_gain:
                    max_gain = gain
                    threshold = sample.features[f_id]
            return max_gain, threshold


    def calc_pure(dataset):
        total_count = len(dataset)
        pos_count = 0
        for sample in dataset:
            if sample.label is True:
                pos_count += 1
        p = float(pos_count) / total_count
        return 2 * p - 2 * p * p



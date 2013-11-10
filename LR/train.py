import sys
import math

class LRTrainer:
    def __init__(self, max_iter, reg_param, alpha, decay, reg_type = "l1"):
        self.max_iter = max_iter
        self.reg_param = reg_param
        self.alpha = alpha
        self.decay = decay
        self.reg_type = reg_type
        self.dataset = []

    def load_dataset(self, filepath):
        self.name2id = {"global_bias" : 0}
        self.id2name = ["global_bias"]
        self.fea_cnt = 0
        for line in open(filepath):
            fields = line.split()
            label = 1 if fields[0] == "1" or fields[0] == "+1" else 0
            fea2value = {}
            for fea in fields[2:]:
                fea_splits = fea.split(":")
                fea_key = fea_splits[0] 
                fea_value = float(fea_splits[1]) if len(fea_splits) is 2 else 1.0
                
                if fea_key in self.name2id:
                    fea_id = self.name2id[fea_key]
                else:
                    self.fea_cnt += 1
                    fea_id = self.fea_cnt
                    self.name2id[fea_key] = fea_id
                    self.id2name.append(fea_key)
                fea2value[fea_id] = fea_value
            fea2value[0] = 1.0
            self.dataset.append((label, fea2value))
        self.sample_cnt = len(self.dataset)
        print "feature count:", self.fea_cnt
        print "dataset size:", self.sample_cnt

    def train(self):
        self.weight_list = [0] * (self.fea_cnt + 1)
        cur_alpha = self.alpha
        sgd_reg_param = self.reg_param / self.sample_cnt
        last_rsme = -1.0
        for i in xrange(self.max_iter):
            for sample in self.dataset:
                #self.sgd_update(sample, cur_alpha, sgd_reg_param) 
                self.sgd_update(sample, cur_alpha, self.reg_param) 
            rsme = self.calc_rmse()
            print "Iterateion", i, ":", rsme, last_rsme - rsme
            if rsme <= last_rsme and last_rsme - rsme <= 0.000001:
                return
            cur_alpha *= self.decay
            last_rsme = rsme
    
    def save_model(self, model_filepath):
        fout = open(model_filepath, "w")
        non_zero_cnt = 0
        for i in xrange(self.fea_cnt + 1):
            if self.weight_list[i] != 0:
                print >>fout, self.id2name[i], self.weight_list[i]
                non_zero_cnt += 1
        print "non_zero_cnt:", non_zero_cnt

    def sgd_update(self, sample, alpha, reg_param):
        label = sample[0]
        fea2value = sample[1]
        predict_value = self.predict(fea2value, self.weight_list)
        error = label - predict_value
        for i in xrange(self.fea_cnt + 1):
            fea_value = fea2value.get(i, 0)
            if self.reg_type == "l2":
                self.weight_list[i] += alpha * (error * fea_value - reg_param * self.weight_list[i])
            else:
                w = self.weight_list[i]
                if w == 0:
                    self.weight_list[i] += alpha * error * fea_value 
                elif w > 0:
                    self.weight_list[i] = max(w + alpha * (error * fea_value - reg_param), 0.0)
                else:
                    self.weight_list[i] = min(w + alpha * (error * fea_value + reg_param), 0.0)
   
    def calc_rmse(self):
        rmse = 0.0
        for sample in self.dataset:
            label = sample[0]
            fea2value = sample[1]
            predict_value = self.predict(fea2value, self.weight_list)
            error = label - predict_value
            rmse += error * error
        return math.sqrt(rmse / len(self.dataset))

    def dot(self, fea2value, weight_list):
        #sum = 0
        #for fea in fea2value.keys():
        #    sum += fea2value[fea] * weight_list[fea]
        return sum([fea2value[fea] * weight_list[fea] for fea in fea2value.keys()])
    
    def predict(self, fea2value, weight_list):
        return 1 / (1 + math.exp(-1 * self.dot(fea2value, weight_list)))
        

def main():
    if len(sys.argv) < 8:                                                          
        print "Usage: %s <training file> <output model file> <max_iter> <alpha> <decay> <reg type(l1|l2)> <reg param>" % __file__
        exit()

    max_iter = int(sys.argv[3])
    alpha = float(sys.argv[4])
    decay = float(sys.argv[5])
    reg_type = sys.argv[6]
    reg_param = float(sys.argv[7])
    lr_trainer = LRTrainer(max_iter, reg_param, alpha, decay, reg_type)
    lr_trainer.load_dataset(sys.argv[1])
    lr_trainer.train()
    lr_trainer.save_model(sys.argv[2])

if __name__ == "__main__":
    main()
    


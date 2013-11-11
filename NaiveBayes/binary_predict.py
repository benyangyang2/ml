import sys
import math

# Only support binary class and binary feature
def main():
    if len(sys.argv) < 4:
        print "Usage: %s <testing file> <model file> <score file>" % __file__
        exit()

    f_model = open(sys.argv[2])
    f_score = open(sys.argv[3], "w")
    p_fea_in_pos = {}
    p_fea_in_neg = {}

    p_positive = float(f_model.readline())
    p_fea_in_pos_new = float(f_model.readline())
    p_fea_in_neg_new = float(f_model.readline())
    lens = (f_model.readline()).split()
    pos_fea_cnt = int(lens[0])
    neg_fea_cnt = int(lens[1])

    for i in range(pos_fea_cnt):
        line = f_model.readline()
        fea = line.split()[0]
        p_fea_in_pos[fea] = float(line.split()[1])
    
    for i in range(neg_fea_cnt):
        line = f_model.readline()
        fea = line.split()[0]
        p_fea_in_neg[fea] = float(line.split()[1])
        
    cnt = 0
    for line in open(sys.argv[1]):
        fields = line.split()
        label = fields[0]
        p_pos = math.log(p_positive)
        p_neg = math.log(1 - p_positive)
        temp_feas = set(p_fea_in_pos.keys()) | set(p_fea_in_neg.keys())
        fea_list = [x.split(":")[0] for x in fields[1:]]
        for fea in p_fea_in_pos.keys():
            p = p_fea_in_pos[fea]
            if fea in fea_list:
                p_pos += math.log(p)
            else:
                p_pos += math.log(1 - p)
        for fea in p_fea_in_neg.keys():
            p = p_fea_in_neg[fea]
            if fea in fea_list:
                p_neg += math.log(p)
            else:
                p_neg += math.log(1 - p)
        p_neg -= p_pos
        p_pos = 0
        score = math.exp(p_pos) / (math.exp(p_pos) + math.exp(p_neg))
        print >>f_score, label, score 


if __name__ == "__main__":
    main()


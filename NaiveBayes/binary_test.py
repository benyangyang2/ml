import sys

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
        
    for line in open(sys.argv[1]):
        fields = line.split()
        label = fields[0]
        p_temp = p_positive / (1 - p_positive)
        temp_feas = set(p_fea_in_pos.keys()) | set(p_fea_in_neg.keys())
        for fea in fields[1:]:
            fea = fea.split(":")[0]
            p_pos = p_fea_in_pos.get(fea, p_fea_in_pos_new)
            p_neg = p_fea_in_neg.get(fea, p_fea_in_neg_new)
            p_temp *= p_pos / p_neg
            if fea in temp_feas:
                temp_feas.remove(fea)
        for fea in temp_feas:
            p_pos = 1 - p_fea_in_pos.get(fea, p_fea_in_pos_new)
            p_neg = 1 - p_fea_in_neg.get(fea, p_fea_in_neg_new)
            p_temp *= p_pos / p_neg
        score = p_temp / (1 + p_temp)
        print >>f_score, label, score 





        


if __name__ == "__main__":
    main()


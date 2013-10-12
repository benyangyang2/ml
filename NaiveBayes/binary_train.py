import sys

# Only support binary class and binary feature
def main():
    if len(sys.argv) < 3:                                                          
        print "Usage: %s <training file> <output model file>" % __file__
        exit()

    total_count = 0
    positive_count = 0
    fea_count_in_pos = {}
    fea_count_in_neg = {}

    for line in open(sys.argv[1]):
        fields = line.split()
        label = fields[0] == "1"

        total_count += 1
        if label:
            positive_count += 1
            for fea in fields[1:]:
                fea = fea.split(":")[0]
                cnt = fea_count_in_pos.get(fea, 0)
                fea_count_in_pos[fea] = cnt + 1
        else:
            for fea in fields[1:]:
                fea = fea.split(":")[0]
                cnt = fea_count_in_neg.get(fea, 0)
                fea_count_in_neg[fea] = cnt + 1

    p_positive = float(positive_count + 1) / (total_count + 2)
    p_fea_in_pos = {}
    p_fea_in_neg = {}
    for fea in fea_count_in_pos.keys():
        cnt = fea_count_in_pos[fea]
        p_fea_in_pos[fea] = float(cnt + 1) / (positive_count + 2)
    for fea in fea_count_in_neg.keys():
        cnt = fea_count_in_neg[fea]
        p_fea_in_neg[fea] = float(cnt + 1) / (total_count - positive_count + 2)
    p_fea_in_pos_new = 1 / float(positive_count + 2)
    p_fea_in_neg_new = 1 / float(total_count - positive_count + 2)

    f_model = open(sys.argv[2], "w")
    print >>f_model, p_positive
    print >>f_model, p_fea_in_pos_new
    print >>f_model, p_fea_in_neg_new
    print >>f_model, len(fea_count_in_pos.keys()), len(fea_count_in_neg.keys())
    for fea in fea_count_in_pos.keys():
        print >>f_model, fea, p_fea_in_pos[fea]
    for fea in fea_count_in_neg.keys():
        print >>f_model, fea, p_fea_in_neg[fea]



        


if __name__ == "__main__":
    main()


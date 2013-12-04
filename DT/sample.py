class DT_Sample:
    def __init__(self, line, fea_cnt):
        self.label = None
        self.features = [None] * fea_cnt
        self.parse(line)

    def parse(self, line):
        fields = line.split()
        self.label = fields[0] == "1"
        try:
            for f in fields[2:]:
                f_id = int(f.split(":")[0])
                f_value = f.split(":")[1]
                self.features[f_id] = f_value
        except:
            print "fea_cnt",len(self.features)
            print "f_id",f_id

    
class BinarySample:
    def __init__(self, line, feature_list):
        self.label = None
        self.features = {}
        self.parse(line, feature_list)

    def parse(self, line, feature_list):
        fields = line.split()
        self.label = fields[0] == "1"
        for f in feature_list:
            self.features[f] = "0"
        for f in fields[2:]:
            f_id = int(f.split(":")[0])
            #f_value = f.split(":")[1]
            self.features[f_id] = "1"
            

def get_pos_count(dataset):
    pos_count = 0
    for sample in dataset:
        if sample.label is True:
            pos_count += 1
    return pos_count



class DT_Sample:
    def __init__(self, line):
        self.label = None
        self.features = {}
        self.parse(line)

    """
    def parse(self, line):
        fields = line.split()
        self.label = fields[14] == "1"
        f_id = 0
        for f in fields[1:13]:
           self.features[f_id] = f
           f_id += 1
    """
    """ 
    def parse(self, line):
        fields = line.strip().split(",")
        self.label = fields[16] == "democrat."
        f_id = 0
        for f in fields[0:16]:
            self.features[f_id] = f
            f_id += 1
    """
    def parse(self, line):
        fields = line.split()
        self.label = fields[0] == "1"
        for f in fields[2:]:
            f_id = int(f.split(":")[0])
            f_value = f.split(":")[1]
            self.features[f_id] = f_value
    
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



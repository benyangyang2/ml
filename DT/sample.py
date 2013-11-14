class DT_Sample:
    def __init__(self, line):
        self.label = None
        self.features = []
        self.parse(line)

    def parse(self, line):
        fields = line.split()
        self.label = fields[0]

def get_pos_count(dataset):
    pos_count = 0
    for sample in dataset:
        if sample.label is True:
            pos_count += 1
    return pos_count



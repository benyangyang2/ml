class FeatureType:
    CONTINUAL = 0
    DISCRETE = 1

class Feature:
    def __init__(self, line):
        self.parse(line)

    def parse(self, line):
        fields = line.split()
        self.id = int(fields[0])
        self.type = FeatureType.DISCRETE if fields[1] == "1" else FeatureType.CONTINUAL 
        if self.type == FeatureType.DISCRETE:
            self.values = fields[2].split(",")
        

class DT_Sample:
    def __init__(self, line):
        self.label = None
        self.features = []
        self.parse(line)

    def parse(self, line):
        fields = line.split()
        self.label = fields[0]



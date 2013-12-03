from tree_node import *
from feature import *
from dt_model import *

class RF_Model:
    def __init__(self):
        self.root = None 
        self.features = {}
        self.dt_models = []

    def add_dt_model(self, dt_model):
        self.dt_models.append(dt_model)

    def predict(self, sample):
        prob_total = 0.0
        for dt_model in self.dt_models:
            prob = dt_model.predict(sample)
            prob_total += prob
        return prob_total / len(self.dt_models)
            

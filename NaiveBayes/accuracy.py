import datetime
import time
import random
import sys
from operator import itemgetter

tp = 0
fp = 0
tn = 0 
fn = 0
for line in file(sys.argv[1]):
    tks = line.strip().split()
    if len(tks) != 2:
        continue
    actual = tks[0] == "1"
    predict = float(tks[1]) >= 0.5

    if actual and predict:
        tp += 1
    elif actual and not predict:
        fn += 1
    elif not actual and predict:
        fp += 1
    else:
        tn += 1
accuracy = float(tp + tn) / (tp + tn + fp + fn)
precision = float(tp) / (tp + fp)
recall = float(tp) / (tp + fn)

print accuracy, precision, recall


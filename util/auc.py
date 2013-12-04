import datetime
import time
import random
import sys
from operator import itemgetter

def auc(result):
    pn = 0
    nn = len(result)
    i = 0
    ret = 0
    count = nn
    for real, pred in sorted(result, key=itemgetter(1), reverse=True):
        if real > 0:
            ret += float(count - i)
            pn += 1
            nn -= 1
        i += 1
    ret2 = float(pn) * float(pn + 1) / 2.0
    return (ret - ret2) / float(pn * nn)

result = []
for line in file(sys.argv[1]):
    tks = line.strip().split()
    if len(tks) != 2:
        continue
    if tks[1].lower() == 'nan':
        continue
    real = float(tks[0])
    pred = random.random() * 0.000001 + float(tks[1])
    result.append((real, pred))

test_auc = auc(result)
print test_auc

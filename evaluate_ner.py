#!/usr/bin/env python

import sys

from sklearn.metrics import classification_report
import re
import pandas as pd

if len(sys.argv) < 2:
    exit(-1)

ofilename = sys.argv[1]

of = open(ofilename, 'r')
output = of.read()
pattern = re.compile(r'(I-.{3,4}|O)\s+(I-.{3,4}|O)\s+')

actual_tags = []
predicted_tags = []
for tag1, tag2 in re.findall(pattern, output):
    actual_tags.append(tag1.strip())
    predicted_tags.append(tag2.strip())

print "CLASSIFICATION REPORT"
print classification_report(actual_tags, predicted_tags)

p_actual = pd.Series(actual_tags)
p_pred = pd.Series(predicted_tags)
print "\nCONFUSION MATRIX"
print pd.crosstab(p_actual, p_pred, rownames=['True'], colnames=['Predicted'], margins=True)
print "\nCONFUSION MATRIX %"
print pd.crosstab(p_actual, p_pred, rownames=['True'], colnames=['Predicted']).apply(lambda r: 100.0 * r/r.sum())

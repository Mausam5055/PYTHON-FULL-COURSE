# import numpy as np
# x=[17,10,9,14,13,17,12,20,14]
# mean=0
# for i in range(len(x)):
#   mean+=x[i]/len(x)
# print(mean)
# import statistics as st
# print("Median", st.median(x))
# print("Mode", st.mode(x))

import statistics
x = [17,10,9,14,13,17,12,20,14]
print("mean", statistics.mean(x))
print("median", statistics.median(x))
print("mode", statistics.mode(x))
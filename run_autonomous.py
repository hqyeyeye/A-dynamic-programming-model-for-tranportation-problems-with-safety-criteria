#run the autonomous model
'''run file'''
from practice import ValueIterationModel
import matplotlib.pyplot as plt
''' change different p and q '''

p = 10
q = 1
g_Cons = 0

b = ValueIterationModel(p,q,g_Cons)
b.readData('data to examine weather and traffic',0)
#find the cost for the optimal policy
c = b.Optimizer(num_of_stage = 16)

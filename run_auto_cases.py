# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 16:05:50 2019

@author: huqio
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 09:12:01 2019

@author: huqio
"""

#run autonomous model
'''run file'''
from practice import ValueIterationModel
import matplotlib.pyplot as plt
''' change different p and q '''

''' change first argument to try a different speed '''
#a.NoStop(75,p,q)
#a.NoRisk(75,p,q)
print("\nThe result of value iteration: ")
#b = ValueIterationModel(p,q)
#b.readData('g_5.22.xlsx',0)
#c1 = b.Optimizer(num_of_stage = 16)
#c1_NoRisk = b.Optimizer(1)
#c_Go = b.Go([55, 55, 55, 0, 0, 0, 0, 55, 75, 75, 75, 75, 75, 75, 55, 75] )
#b = ValueIterationModel(p,q)
#b.readData('g_5.22.xlsx',1)
#c2 = b.Optimizer(num_of_stage = 16)
#
#b = ValueIterationModel(p,q)
#b.readData('g_5.22.xlsx',2)
#c3 = b.Optimizer(num_of_stage = 16)
#
#b = ValueIterationModel(p,q)
#b.readData('g_5.22.xlsx',3)
#c4 = b.Optimizer(num_of_stage = 16)
# 
#b = ValueIterationModel(p,q)
#b.readData('g_5.22.xlsx',4)
#c5 = b.Optimizer(num_of_stage = 16)
#
#fig,axs = plt.subplots() 
#axs.plot(c1, '-ko', label = 'base')
#axs.plot(c2, '-bo', label = 'case1')
#axs.plot(c3, '-go', label = 'case2')
#axs.plot(c4, '-ro', label = 'case3')
#axs.plot(c5, '-co', label = 'case4')
#
##axs.plot(g4, '-bo', label = 'starting when g is 0')
##
##axs.set_title('g plot')
#axs.set_xlabel('stage')
#axs.set_ylabel('cost')
#legend = fig.legend(loc='upper right', shadow=True, fontsize = 'x-large', ncol=2)
#legend.get_frame().set_facecolor('white')
#fig.show()

p = 10
q = 1
g_Cons = 0

#b = ValueIterationModel(p,q,g_Cons)
#b.readData('data_6.21.xlsx',0)
#c1_a = b.Optimizer(num_of_stage = 16)
#
#b = ValueIterationModel(p,q,g_Cons)
#b.readData('data_6.21.xlsx',1)
#c2_a = b.Optimizer(num_of_stage = 16)
###
#b = ValueIterationModel(p,q,g_Cons)
#b.readData('data_6.21.xlsx',2)
#c3_a = b.Optimizer(num_of_stage = 16)
##
#b = ValueIterationModel(p,q,g_Cons)
#b.readData('data_6.21.xlsx',3)
#c4_a = b.Optimizer(num_of_stage = 16)
# 
b = ValueIterationModel(p,q,g_Cons)
b.readData('data_6.21.xlsx',4)
c5_a = b.Optimizer(num_of_stage = 16)
#
#from valueiteration_write import ValueIterationModel
#p = 10
#q = 1
#g = 0
#gNone = 0.5
#b = ValueIterationModel(p,q,g,gNone)
#b.readData('data_6.21.xlsx',8)
#g1,c1 = b.Optimizer(num_of_stage = 16)
#
#b = ValueIterationModel(p,q,g,gNone)
#b.readData('data_6.21.xlsx',1)
#g2,c2 = b.Optimizer(num_of_stage = 16)
#
#b = ValueIterationModel(p,q,g,gNone)
#b.readData('data_6.21.xlsx',2)
#g3,c3 = b.Optimizer(num_of_stage = 16)
#
#b = ValueIterationModel(p,q,g,gNone)
#b.readData('data_6.21.xlsx',3)
#g4,c4 = b.Optimizer(num_of_stage = 16)
##
#b = ValueIterationModel(p,q,g,gNone)
#b.readData('data_6.21.xlsx',4)
#g5,c5 = b.Optimizer(num_of_stage = 16)
#
#
#fig,axs = plt.subplots() 
#axs.plot(c1_a, '-ko', label = 'Autonomous_base')
#axs.plot(c2_a, '-bo', label = 'Autonomous_case1')
#axs.plot(c3_a, '-go', label = 'Autonomous_case2')
#axs.plot(c4_a, '-ro', label = 'Autonomous_case3')
#axs.plot(c5_a, '-co', label = 'Autonomous_case4')
##
##
#axs.plot(c1, '-k+', label = 'Human-Drive_base')
#axs.plot(c2, '-b+', label = 'Human-Drive_case1')
#axs.plot(c3, '-g+', label = 'Human-Drive_case2')
#axs.plot(c4, '-r+', label = 'Human-Drive_case3')
#axs.plot(c5, '-c+', label = 'Human-Drive_case4')
#plt.tick_params(labelsize=20)
#axs.set_title('6.21 4 cases_gCons is 0', fontsize=24)
##axs.set_title('Risk Cost_1-4segments_2-6hours_gConstant0.5')
#axs.set_title('Comparison between Autonomous-Human when gConstant is 0.5')
#
#axs.set_xlabel('stage',fontsize=22)
#axs.set_ylabel('cost',fontsize=22)
#legend = fig.legend(loc='upper right', shadow=True, fontsize = 18, ncol=2)
#legend.get_frame().set_facecolor('white')
#fig.show()


#from valueiteration_write import ValueIterationModel
#p = 10
#q = 1
#g = 0
#gNone = 0.5
#b = ValueIterationModel(p,q,g,gNone)
#b.readData('data_6.21.xlsx',6)
#g1,c1 = b.Optimizer(num_of_stage = 20)
#fig,axs = plt.subplots() 
#axs.plot(c1_a, '-ko', label = 'Autonomous')
#axs.plot(c1, '-bo', label = 'Human-Drive')
##axs.plot(g4, '-bo', label = 'starting when g is 0')
##
#axs.set_title('Risk Cost_5-8segments_0-4hours_gConstant0.5')
#axs.set_xlabel('stage')
#axs.set_ylabel('cost')
#legend = fig.legend(loc='upper right', shadow=True, fontsize = 'x-large', ncol=2)
#legend.get_frame().set_facecolor('white')
#fig.show()
#c_Go = b.Go()
#c1_Norisk = b.Optimizer(1)
#fig,axs = plt.subplots() 
#axs.plot(c1, '-ko', label = 'base')
#axs.plot(c2, '-bo', label = 'case1')
#axs.plot(c3, '-go', label = 'case2')
#axs.plot(c4, '-ro', label = 'case3')
#axs.plot(c5, '-co', label = 'case4')
#
##axs.plot(g4, '-bo', label = 'starting when g is 0')
##
##axs.set_title('g plot')
#axs.set_xlabel('stage')
#axs.set_ylabel('cost')
#legend = fig.legend(loc='upper right', shadow=True, fontsize = 'x-large', ncol=2)
#legend.get_frame().set_facecolor('white')
#fig.show()

#
#fig,axs = plt.subplots() 
#axs.plot(c1, '-ko', label = 'optimal')
#axs.plot(c4, '-bo', label = 'starting when g is 0')
#axs.set_title('cost plot')
#axs.set_xlabel('stage')
#axs.set_ylabel('cost')
#legend = fig.legend(loc='upper right', shadow=True, fontsize = 'x-large', ncol=2)
#legend.get_frame().set_facecolor('white')
#fig.show()




# =============================================================================
# decision = None
# while (decision != 'y' and decision != 'n'): 
#     decision = raw_input("Do you want to print all states(y/n): ")
#     if decision == 'y':
#         print("\nAll states will be printed below\n")
#         a.printStage()
#     elif decision == 'n':
#         break
# =============================================================================
        

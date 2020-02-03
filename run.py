'''run file'''
from valueiteration_write import ValueIterationModel
#from PetModel import PetModel
import matplotlib.pyplot as plt
#a = PetModel()
''' change different p and q '''

p = 1
q = 1
g = 1.5
gNone = 2

# =============================================================================
# p = float(input("Please insert p: "))
# q = float(input("Please insert q: "))
# =============================================================================
#print("\nThe result of original optimization: ")
#
#''' If you want to use a different dataset, replacing 'data.xlsx' with your filename'''
#
#a.readData('g_5.22.xlsx',0)
#print(a.parameter)
#print(a.stage)
#print(a.distance)
#a.printStage()
#a.ObjectiveOptimization(p,q)
#import matplotlib.pyplot as plt
#a.readData('data.xlsx',1)
''' change first argument to try a different speed '''
#a.NoStop(75,p,q)
#a.NoRisk(75,p,q)
#print("\nThe result of value iteration: ")
b = ValueIterationModel(p,q,g,gNone)
b.readData('data_6.21.xlsx',0)
print('gNone is', gNone, ',', 'g is', g )
g1,c1 = b.Optimizer(num_of_stage = 16)
###g4,c4 = b.Go([0, 55, 0, 75, 75, 75, 75, 75, 75, 55, 75, 55, 55, 0, 0, 75] )
#
#print('---------------------------------')
#g2,c2 = b.Optimizer(1)
#if g2 == None:
#    g2 = [0] * len(g1)
#    c2 = [0] * len(g1)
#print('---------------------------------')
#g3,c3 = b.NoStop()
#
##
#fig, axs = plt.subplots(2,1)   
#
##axs[0].plot(g1, '-rD', g2, '-bs', g3, '-g^')
#axs[0].plot(g1, '-r', label = 'optimal')
##axs[0].plot(g4, '-rD', label = 'certain')
#axs[0].plot(g2, '--b', label = 'no risk')
#axs[0].plot(g3, '-.g', label = 'no stop')
#axs[0].set_title('g plot')
#axs[0].set_xlabel('stage')
#axs[0].set_ylabel('g')
##axs[1].plot(c1, '-rD', c2, '-bs', c3, '-g^')
#axs[1].plot(c1, '-rD', label = 'optimal')
##axs[1].plot(c4, '-rD', label = 'certain')
#axs[1].plot(c2, '-bs', label = 'no risk')
#axs[1].plot(c3, '-g^', label = 'no stop')
#axs[1].set_xlabel('stage')
#axs[1].set_title('cost plot')
#axs[1].set_ylabel('cost')
#plt.subplots_adjust(hspace=0.8)
#fig.legend(loc='upper center', bbox_to_anchor=(0.5, 1.00), shadow=True, ncol=2)
#fig.show()
#q_list=[0.01,0.02,0.03,0.04,0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,
#        23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
#b.pqratio_plot(q_list,16)
#q_list=[0.01,0.02,0.03,0.04,0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,
#        ]
#b.pqratio_plot(q_list,16)    

#fig,axs = plt.subplots() 
#axs.plot(c1, '-ko', label = 'optimal')
##axs.plot(g4, '-bo', label = 'starting when g is 0')
##
##axs.set_title('g plot')
#axs.set_xlabel('stage')
#axs.set_ylabel('cost')
#legend = fig.legend(loc='upper right', shadow=True, fontsize = 'x-large', ncol=2)
#legend.get_frame().set_facecolor('white')
#fig.show()
#
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
        

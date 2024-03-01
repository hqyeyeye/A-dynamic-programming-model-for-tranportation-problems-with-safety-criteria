'''run file'''
from valueiteration_write import ValueIterationModel
import matplotlib.pyplot as plt
''' change different p and q '''

p = 1.0
q = 1.0
g = 0

print("\nThe result of value iteration: ")
b = ValueIterationModel(p,q,g)
#first case
print ("Case 1:")
b.readData('data_6.21.xlsx',1)
#g11, c11 is the first case and the optimal policy
g11,c11 = b.Optimizer(num_of_stage = 16)

print('---------------------------------')
g12,c12 = b.Optimizer(1)
if g12 == None:
    g12 = [0] * len(g11)
    c12 = [0] * len(g11)
print('---------------------------------')
g13,c13 = b.NoStop()

#second case
print ("Case 2:")
b.readData('data_6.21.xlsx',2)
#g21, c21 is the second case and the optimal policy
g21,c21 = b.Optimizer(num_of_stage = 16)

print('---------------------------------')
g22,c22 = b.Optimizer(1)
if g22 == None:
    g22 = [0] * len(g21)
    c22 = [0] * len(g21)
print('---------------------------------')
g23,c23 = b.NoStop()

#third case
print ("Case 3:")
b.readData('data_6.21.xlsx',3)
#g31, c31 is the third case and the optimal policy
g31,c31 = b.Optimizer(num_of_stage = 16)

print('---------------------------------')
g32,c32 = b.Optimizer(1)
if g32 == None:
    g32 = [0] * len(g31)
    c32 = [0] * len(g31)
print('---------------------------------')
g33,c33 = b.NoStop()

#fourth case
print ("Case 4:")
b.readData('data_6.21.xlsx',4)
#g41, c41 is the first case and the optimal policy
g41,c41 = b.Optimizer(num_of_stage = 16)

print('---------------------------------')
g42,c42 = b.Optimizer(1)
if g42 == None:
    g42 = [0] * len(g41)
    c42 = [0] * len(g41)
print('---------------------------------')
g43,c43 = b.NoStop()


fig, axs = plt.subplots()   

axs.plot(g11, '-ko', label = 'case 1 optimal')
axs.plot(g12, '--k^', label = 'case 1 no risk')
axs.plot(g13, '-.kd', label = 'case 1 no stop')

axs.plot(g21, '-bo', label = 'case 2 optimal')
axs.plot(g22, '--b^', label = 'case 2 no risk')
axs.plot(g23, '-.bd', label = 'case 2 no stop')

axs.plot(g31, '-go', label = 'case 3 optimal')
axs.plot(g32, '--g^', label = 'case 3 no risk')
axs.plot(g33, '-.gd', label = 'case 3 no stop')

axs.plot(g41, '-ro', label = 'case 4 optimal')
axs.plot(g42, '--r^', label = 'case 4 no risk')
axs.plot(g43, '-.rd', label = 'case 4 no stop')

axs.set_title('g plot')
axs.set_xlabel('stage')
axs.set_ylabel('g')
plt.subplots_adjust(hspace=0.8)
legend = fig.legend(loc='upper right', shadow=True, fontsize = 'x-large')
legend.get_frame().set_facecolor('white')
fig.show()

fig, axs = plt.subplots()
axs.plot(c11, '-ko', label = ' case 1 optimal')
axs.plot(c12, '--k^', label = 'case 1 no risk')
axs.plot(c13, '-.kd', label = 'case 1 no stop')

axs.plot(c21, '-bo', label = ' case 2 optimal')
axs.plot(c22, '--b^', label = 'case 2 no risk')
axs.plot(c23, '-.bd', label = 'case 2 no stop')

axs.plot(c31, '-go', label = ' case 3 optimal')
axs.plot(c32, '--g^', label = 'case 3 no risk')
axs.plot(c33, '-.gd', label = 'case 3 no stop')

axs.plot(c41, '-ro', label = ' case 4 optimal')
axs.plot(c42, '--r^', label = 'case 4 no risk')
axs.plot(c43, '-.rd', label = 'case 4 no stop')


axs.set_xlabel('stage')
axs.set_title('cost plot')
axs.set_ylabel('cost')
plt.subplots_adjust(hspace=0.8)
legend = fig.legend(loc='upper right', shadow=True, fontsize = 'x-large')
legend.get_frame().set_facecolor('white')
fig.show()
  

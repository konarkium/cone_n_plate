import os
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches

# fix font to 14 and make it so it's editable PDF
mpl.rcParams['pdf.fonttype'] = 42
mpl.rcParams['font.size'] = 14

# %% detecting file
filename = 'cone_n_plate.csv'
for f in os.listdir(r'C:/Users/konar/.spyder-py3'):
    if f == filename:
        print('the file exists')
        break
    else:
        print('file not found')

# %%

df = pd.read_csv(filename)

sample_number = 7 #int(input("enter number of samples: "))
samples = np.arange(1, sample_number+1)

names = ['0%', '5%', '10%', '15%', '20%', '25%', '30%']
        #[str(x) for x in input('Enter names of samples seperated by commas: ').split(',')]
parameters = ['SR','SS','V','S','T']
               #x   y   y   x    y 

list_var = []
for par in parameters:
    for i,n in enumerate(names,1):
        var = df[par+str(i)].dropna()
        list_var.append(var)
        
#%%

#Prepare multipanel plot 
fig = plt.figure(1, figsize=(5, 10))
#prepare grid
gs = gridspec.GridSpec(9,5)
#determine gap dimentions
gs.update(hspace=0.0005)   

#%% speed vs torque (not included)

# plt.loglog(list_var[21], list_var[28])
# plt.xlabel('speed')
# plt.ylabel('torque')

#%% shear rate vs shear stress

xtr_subplot = fig.add_subplot(gs[0:5,0:5])

for i in samples:
    plt.loglog(list_var[i-1],list_var[i+6],
               c='black', alpha = (i+1)/10,
               label = names[i-1])

plt.minorticks_on()
plt.tick_params(which='minor', direction='in', length=5, 
                bottom=True, top=False, left=True, right=False)

plt.tick_params(which='major', direction='in', length=10, 
                bottom=True, top=False, left=True, right=False)

plt.tick_params(labelbottom=False, labeltop=False,
                labelleft=True, labelright=False)

plt.ylabel('shear stress (Pa)')

#%% shear rate vs viscocity

xtr_subplot = fig.add_subplot(gs[5:9,0:5])

for i in samples:
    plt.loglog(list_var[i-1],list_var[i+13], 
               c='black', alpha = (i+1)/10,
               label = names[i-1])

plt.minorticks_on()
plt.tick_params(which='minor', direction='in', length=5, 
                bottom=True, top=False, left=True, right=False)

plt.tick_params(which='major', direction='in', length=10, 
                bottom=True, top=False, left=True, right=False)

plt.tick_params(labelbottom=True, labeltop=False,
                labelleft=True, labelright=False)
           
plt.xlabel('shear rate (s$^-$$^1$)')
plt.ylabel('viscosity (Pa.s$^-$$^1$)')

plt.legend()

#%%

plt.savefig('cone_n_plate.png', dpi=300,bbox_inches="tight")

















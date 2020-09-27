# Data Preprocessing Template

# Importing the libraries
import numpy as np
import excel
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split

import pandas as pd
from tablib import Dataset
import numpy as np
import matplotlib.pyplot as plt



# Importing the dataset
dataset = pd.read_csv('Data.xlsx', error_bad_lines=False)
#X = dataset.iloc[:, :-1].values
#y = dataset.iloc[:, -1].values
#dates_row = dataset.loc[4, :]
#xt = pd.Series(dates_row).values
nx = pd.read_excel('Data.xlsx')
df = pd.DataFrame(nx, columns= ['Name', 'P Number'])
Names = []
pNumbers = []

filtered_names = []
filtered_pNumbers = []

def show_table(names, numbers):
    for i in range(len(names)):
        print names[i] + " | " + numbers[i]
        print "--------------------------------"
        
for i in range(len(df['Name'])):
    #print df['Name'][i]
    Names.append(df['Name'][i])
    pNumbers.append(df['P Number'][i])
    
print "Append to database one row values using forloop"
for x in range(len(Names)):
    name = str(Names[x])
    pr = str(pNumbers[x])
    #filter
    if name == 'nan':
        name = '------'
        filtered_names.append(name)
        
    else:
        filtered_names.append(name)
        
        
    if pr == 'nan':
        pr = '------'
        filtered_pNumbers.append(pr)
        
    else:
        filtered_pNumbers.append(pr)
        
            
def runner():
    show_table(filtered_names, filtered_pNumbers)
runner()
#print df.iloc[0]

#print df['Name']




# Splitting the dataset into the Training set and Test set
#from sklearn.model_selection import train_test_split
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

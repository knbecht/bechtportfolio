import os.path

# Get the directory name for data files
directory = os.path.dirname(os.path.abspath(__file__))  

name1='US Highway Fatalities per million'
name2='US Fatality rates per Registered Motor Vehicles per 100,000'

#initialize the aggregators
years1=[]
number_of_fatalities=[]
years2=[]
number_of_register=[]

# Scan one  file at a time
#for year in range(1900,2015):
# Open the file
filename = os.path.join(directory,'fatalitiesdatav1.txt')
datafile = open(filename,'r')
# Go through all the names that year
#datafile = open('fatalitiesdatav1.txt','r')
for line in datafile: 
    year1, number_of_fatality = line.split(',')
    years1+=[year1]
    number_of_fatalities+=[number_of_fatality]
datafile.close()  
filename = os.path.join(directory, 'registrationdatav1.txt')
datafile = open(filename,'r')
#datafile = open('registrationdatav1.txt','r') 
# Go through all the names that year
for line in datafile:
    year, number_of_registered_vehicles = line.split(',')
    years2+=[year]
    number_of_register+=[number_of_registered_vehicles]    
datafile.close()  

          
# Plot on one set of axes.
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1,1)
ax.plot(years1,number_of_fatalities,'#FF0000')
ax.plot(years2,number_of_register,'#000000')

ax.set_title('U.S. Car Fatality Data ' +
             name1 + ' (Red) or ' + name2 + ' (black)')
fig.show()
# Importing repositries
import csv
import random

# DEBUG
#task_number = random.randint(0, 10) #Giving me random lines

# Importing routine file
raw_morning_data = open('morn_data.csv') #importing the data raw
read_morning_data = csv.reader(raw_morning_data) #reading the data raw
row = list(read_morning_data) #creating each data row
row_count = len(row) #the total number of rows in the list

#THIS IS THE MONEY SHOT BABY
#print(row) #clearing the line
#string_row = str(row[task_number])[2:-2]
#print(string_row)

# Setting initiated variables / RANDOM NUMBERS
total_tasks = random.randint(0, 10) #choosing between 0 - 10 
task_number = random.randint(0, total_tasks) #choosing between 0 - 10 
task_counter = total_tasks

#setting constant variables
x = 1
total_time = 0


'''
def routines(x):
    print(x)
    x = x -1
    #print("ROUTINE RUNNING!")
    print(x)
    global task_counter = int(x)
    #string_row = str(row[task_number])[2:-2]
    #print(string_row)
'''
'''
def mainloop(task_counter):
    if(task_counter != 0):
        while task_counter != 0:
            routines(task_counter)
            print("does not equal")
            print(task_counter)
    else:
        print("All done!")
'''
'''
while task_counter != int(0):
    routines(task_counter)
    #task_counter = int(x)
    #print("does not equal")
    print(task_counter)
    break
else:
    print("All done!")
'''

# START - program introduction
print()
print(r"Good morning, todays morning routine consists of", total_tasks, "tasks.")
print()
#print(task_counter)
#mainloop(task_counter)
#if(task_counter != 0):

while task_counter != 0:
    time = random.randint(1, total_tasks) #choosing between 0 - 10 
    total_time = total_time + time
    str_time = "(" + str(time) + 'min)'
    task_counter = task_counter -1
    #print(task_counter)
    y = str(x) + "."

    #THIS IS THE MONEY SHOT BABY
    #print(row) #clearing the line
    task_number = random.randint(0, total_tasks) #choosing between 0 - total
    string_row = str(row[task_number])[2:-2]
    #print(string_row)
    print(y, string_row, str_time)
    x = x +1
    #break
else:
    #print("All done!")
    print(" ")
    final_total_time = "Todays morning routine will take: " + str(total_time) + " min's"
    print(final_total_time)
    print(" ")

    
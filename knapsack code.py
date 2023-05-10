import os 

def constructive():     
    knapsack = []
    Weight = 0
    while(Weight <= cap):
        best = max(values)
        i = values.index(best)
        knapsack.append(i)
        Weight = Weight + weights[i]
        del values[i]
        del weights[i]
    return knapsack, Weight


def read_kfile(fname):
    with open(fname, 'rU') as kfile:
        lines = kfile.readlines()     # reads the whole file
    n = int(lines[0])
    c = int(lines[n+1])
    vs = []
    ws = []
    lines = lines[1:n+1]   # Removes the first and last line
    for l in lines:
        numbers = l.split()   # Converts the string into a list
        vs.append(int(numbers[1]))  # Appends value, need to convert to int
        ws.append(int(numbers[2]))  # Appends weigth, need to convert to int
    return n, c, vs, ws

dir_path = os.path.dirname(os.path.realpath(__file__))  # Get the directory where the file is located
os.chdir(dir_path)  # Change the working directory so we can read the file

knapfile = 'knap20.txt'
nitems, cap, values, weights = read_kfile(knapfile)
val1,val2 =constructive()
print ('knapsack',val1)
print('weight', val2)
print('cap', cap)

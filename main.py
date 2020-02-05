# Election Prediction AI - developed to predict the 2020 US Senate Elections
# Jack Preble
# Jan. 24, 2020
# Why is ATCS hard, Mr. Cochran??

'''import geopandas as gpd
import matplotlib.pyplot as plt'''

import datetime
from election import *
from candidate import *

senators = []
elections = []

class1 = []
class2 = []
class3 = []

class1yr = 2018
class2yr = 2020
class3yr = 2022

currentyr = int(datetime.datetime.now().year) #https://www.quora.com/How-do-I-get-the-current-year-as-an-int-value-in-Python

roster_f = open('senators-set.csv')

for line in roster_f:
    line = line.strip()
    senators.append(line.split(','))

f = [line.rstrip('\n') for line in open('1976-2018-senate.tab')] # from Shan
for i in range(len(f)):
    f[i] = f[i].split('\t')


def fileSort():
    global f

    for e in range(len(f)):
        #print('DEBUG ' + str(e))
        f[e] = [f[e][0], f[e][1], f[e][11],
                f[e][14], f[e][15]]

    for e in reversed(f):
        if "NA" in e[2]:
            f.pop(f.index(e))


fileSort()

for e in f:
    print(e)

'''print('debug 1')

for e in f:
    print('LINE 58:',e)
    elections += [Election(int(e[0]),e[1],int(e[5])]

print('debug 2')

print(elections)'''


'''def electionSort():
    global elections_f
    global elections

    for e in elections_f:
        i = 1

        if e == elections_f[0] or elections_f[i-1][0] and e[1] == elections_f[i-1][1]:
            elections += [Election(e[0], e[1], e[15])]
            if e[0] != elections_f[i-1][0] and e[1] != elections_f[i-1][1]:
                i += 1
                print('debug:', i)
            continue
        else:
            print('debug 2')


electionSort()'''






'''for line in elections_f:
    try:
        line = line.strip().split('\t')
        if line[1] not in elections_MASTER and line[0] not in elections_MASTER:
            elections_MASTER.append(Election(line[0],line[1], False if line[9] == 'FALSE' else True, line[15]))
        else:
            elections_MASTER[-1].add_candidate(Candidate(line[10], line[11], line[14]))
    except Exception as e:
        print(e)
        break



for line in elections_f:
    try:
        line = line.strip().split('\t')
        if line[0] not in elections_MASTER and line[1] not in elections_MASTER:



for election in elections_MASTER:
    print(str(election))


def arrangeClass():
    global senators, class1, class2, class3, escore

    for senator in senators:
        if senator[4] == '1':
            class1.append(senator)
        elif senator[4] == '2':
            class2.append(senator)
        else:
            class3.append(senator)


def electionYear():
    global class1yr, class2yr, class3yr, escore

    if class1yr == currentyr or ((currentyr - class1yr)/6) == int:
        escore += 1
    if class2yr == currentyr or ((currentyr - class2yr) / 6) == int:
        escore += 2
    else:
        escore += 3

def elections():
    global election_results, class1, class2, class3, class1yr, class2yr, class3yr
    for election in reversed(election_results):
        if int(election[0]) < 2010:
            del election_results[election_results.index(election)]
    election_results.sort(key = lambda election_results: election_results[1])



    for election in election_results:
        print(election)



def main():
    arrangeClass()
    electionYear()

if __name__ == "__main__":
    main()'''

#elections()



'''for election in election_results:
    print(election)'''
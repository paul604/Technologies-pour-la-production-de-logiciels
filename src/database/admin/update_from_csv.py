
import csv

def up_installations():
    '''

    '''
    file = open('../../../data/csv/installations.csv','r')
    read = csv.reader(file ,delimiter=',')
    for row in read:
        print(row)
		#tuple dans tab

up_installations()

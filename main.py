import glob
import csv
from random import *

def salaire(grade):
    if grade=='A':
       return randint(200001,350000)
    elif grade=='B':
       return randint(150001,200000)
    elif grade=='C':
       return randint(75001,150000)
    else:
       return randint(40000,75000)
    
   
i=0
header=['matricule','first_name','last_name','date_naiss','gender','ministry','grade','diff_recens','diff_conges','diff_travail','actif','salaire','fraude']
with open("new.csv",'w',newline='') as cea:
  writer=csv.writer(cea,delimiter=",")
  writer.writerow(header)
  with open('agent.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
      if i!=0:
         line.append(salaire(line[6]))
         list_df=line
         if(int(line[7])>=15901200 or int(line[8])>=2592000 or int(line[9])>=1893456000 or line[10]=='0'):
             line.append("fraude")
         else:
            line.append("pas fraude")
         print(list_df)
         writer.writerow(line)
      i=i+1
  csv_file.close()
cea.close()

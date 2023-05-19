import os
import csv 

dir="C:/Users/Carré Vilmorin/Desktop/Synthetic_dataset/Extration"
#obtain the list of name file
listfiles = [f for f in os.listdir(dir) if (os.path.isfile(os.path.join(dir, f)) and os.path.splitext(f)[1] == '.csv')]
#print the name of the list
listfiles=sorted(listfiles,reverse=False)
listfiles.sort()
#print(listfiles)

header=['table','Nom source','Language','pays','Auteurs','Date de publication','Description du contenu','Technique utilisee pour la collecte','Page start','Page end']

with open('file.csv','w',newline='') as file:
    writer=csv.writer(file,delimiter=',')
    writer.writerow(header)
    """for i in listfiles:
        writer.writerow([i,'English','2021','automatic with collab'])"""
    with open('export.csv','r') as export:
            reader=csv.reader(export)
            i=0
            add=[]
            for line in reader:
                if i!=0:
                    ajout=[f'KNSR{line[0]}.pdf',line[4]+' '+line[5]+'('+line[6]+')','English','',line[1],line[3],line[2],"automatic with collab",line[8],line[9]]
                    add.append(ajout)
                i=i+1
            add=sorted(add,reverse=False)
            for l in  add:
                 writer.writerow(l)
    export.close()
file.close()

print(add)
    

#rename each file
""""
for i in range(len(listfiles)):
    old_file = os.path.join(dir,listfiles[i])
    new_file = os.path.join(dir, f'KNSR{i+1}.pdf')
    os.rename(old_file, new_file)
"""
fout=open("combinedDataset.csv","a")
# first file:
for line in open("atharva.csv"):
    fout.write(line)
# now the rest:   
files = ['mayank.csv','siddesh.csv','sidhant.csv'] 
for file in files:
    f = open(file,'r')
    for line in f:
         fout.write(line)
    f.close() # not really needed
fout.close()
# script to read in patch notes file and construct a class for each champion
import json

# array to store lines grabbed from patch file
lines = []
with open("patchExample.dat",'r') as file:
  lines=file.readlines()

# go through every line and grab the champion name.
# make a dictionary with the grabbed champion name strings.
# do this for every grabbed champion name 
for i in range(len(lines)):
    championDict=json.loads(lines[i])
    


#reader class
#https://stackoverflow.com/questions/53320837/reading-class-objects-from-a-txt-file-in-python
class Reader:
  def reader(self,input_dict,*kwargs):
    for key in input_dict:
      try:
        setattr(self, key, input_dict[key])
      except:
        print("no such attribute,please consider add it at init")
        continue



reader_instance=Reader()
reader_instance.reader(championDict)

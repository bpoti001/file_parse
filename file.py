fi = open("D://present_locations.txt",'r') #file reader
present=[] # a list to store all locations in script
for line in fi:
    present.append(line.strip()) #strips is \n from a line
fi.close()
count_of_first_file = len(present)
prefix ='string_to_append_in_start'
postfix ='string_to_append_in_end'
updated=[] #list to store new locations
for i in present:
    updated.append(prefix+' '+i+' '+postfix) # + is used to concatinate strings in python empyt '' indecates space

fo = open('D://udpated_file_locations.txt','w')
for i in updated:
    fo.write('%s\n' %(i))
fo.close()

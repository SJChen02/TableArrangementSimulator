

#Change this value to number of people
TotalNumberOfPPl = 10

# DO NOT CHANGE ANYTHING BELOW!!!! =======================================================================================================================
Half = int(TotalNumberOfPPl/2)+1

row1 = list(range(1,Half))
row2 = list(range(Half,TotalNumberOfPPl+1))
met = [[] for _ in range(TotalNumberOfPPl)] #generates number of list based on number of people

def meeting(j):                 #function that append already met "people" into list of each "numbered"
    if (j in row1):
        pos = row1.index(j)
        met[j-1].append(row2[pos])
    else:
        pos = row2.index(j)
        met[j-1].append(row1[pos])

TotalRotation = len(row1)+len(row2)
for i in range(0,TotalRotation):    #-1 to TotalRotation then it will be the total amount of rotation needed before facing an already met person
    print("Round: "+str(i))
    print(row1)
    print(str(row2) + "\n")
    for j in range(1,TotalNumberOfPPl+1): #+1 so it actually include the final person
        meeting(j)
    row1.insert(1,row2[0])
    row2.append(row1[-1])
    row1.remove(row1[-1])
    row2.remove(row2[0])
    
 
for lists in met:
    print(f"""{met.index(lists)+1} met has with: {lists}
          """)

        
    
    




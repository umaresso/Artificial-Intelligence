# Task 1
def removeValue(sampleList, val):
  retValue =  [ num for num in sampleList if num!=val]
  return retValue
  pass
print(removeValue([1,2,3,2,23,4,1,2],2))
# LAB (end solution)

# Task 2
def findAndReplaceValue(sampleList, val):
  
  length = len(sampleList);
  counter=0;


  while counter<length:
    if(sampleList[counter]==val):
      sampleList[counter]=200
    counter=counter+1;
  pass
  return sampleList;  
  # LAB (end solution)
print(findAndReplaceValue([1,2,3,2,23,4,1,2],2 ))

# Task 3
def vehicleWeight(vehicleDict):
  return [x.upper() for x,y in vehicleDict.items() if y>5000]
  pass
  # LAB (end solution)
print(vehicleWeight({"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}))

# Task 4
def sortTuple(tupleSort):
  return sorted(tupleSort)  
  pass
  # LAB (end solution)
sortTuple((3,2,43))

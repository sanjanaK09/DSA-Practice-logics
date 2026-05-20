#remove leading 0 from the list
#input:[0,0,1,2,0,3,0,0,4]
#remove Leading Zero
def removeLeadingZero(arr):
    for i in range(0,len(arr)):
        if arr[i]!=0:
            return arr[i:]
arr=[0,0,1,2,0,3,0,0,4]   
print(removeLeadingZero(arr))   


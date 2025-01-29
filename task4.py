def find_largest (array) :
    largest = array[0]
    for i in range (0,n):
        if array[i]>largest:
            largest=array[i]
    return largest

def count_occurences(array,largest):
    counter=0
    for j in range (0,n):
         if array[j]==largest:
            counter+=1

    return counter
def is_symmetric (array, largest,n):

    if (n%2==0):
        return False
    else:
       for i in range (0,n):  #O(n)
           if array[i]==largest:
            index=i
            break

       if index!=(n//2):
            return False
       else:
          for j in range(0,n):
                  if array[j]!=array[n-1-j]:
                      return False
          return True








print("Happy birthday to you")
n= int (input("enter your new age"))
array=[]
for i in range(0,n):
    element  =int(input(f"enter element of array which is candles length{i+1}:"))
    array.append(element)
largest=find_largest(array)
print(f"The largest length of candles is: {largest}")
x = count_occurences(array, largest)
print(f"Largest is repeated for {x} times ")
if (is_symmetric(array,largest,n)):
    print("True")
else:
    print("False")



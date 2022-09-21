def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

alist= [53,25,93,17,77,31,43,55,21,27,87,33,9,97,45,57,67,71,39,99,23,35,37,47,41,51,91,3,5,29]
insertionSort(alist)
print(alist)
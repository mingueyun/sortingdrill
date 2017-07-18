
#-----1
listWords = [67, 45, 2, 13, 1, 998]
listOccurrences = [89, 23, 33, 45, 10, 12, 45, 45, 45]
dict = {}
i=0
for listWords, listOccurrences in dict.items() :
    while(len(listWords) > i):
        dict[listWords[i]] = listOccurrences[i];
        i = i + 1

# i was able to print it but it used sort and even it was still buggy and didnt get what i wanted
#I couldnt figure out how to print from dict the key and values 
#the dict wouldnt combine both lists and the left over values
# was left out so i did  drill below to append the empty key and values
#-----1



print('1: 1 and 2 i could not figure out so i made some notes and would like some input')
#-----2


list_1 = [67, 45, 2, 13, 1, 998]
list_2 = [89, 23, 33, 45, 10, 12, 45, 45, 45]
deck = []

for i in range(max((len(list_1),len(list_2)))):
        while True:
            try:
                card = (list_1[i],list_2[i])
            except IndexError:
                if len(list_1)>len(list_2):
                    list_2.append('')
                    card = (list_1[i],list_2[i])
                elif len(list_1)<len(list_2):
                    list_1.append('')
                    card = (list_1[i], list_2[i])
                continue
            deck.append(card)
            break

print('2: still doesnt work', deck)
#>>>[(67, 89), (45, 23), (2, 33), (13, 45), (1, 10), (998, 12), ('', 45), ('', 45), ('', 45)]

#i tried to put  lists into dictionaries, tuples and list
#but i ran into issues with pairs for dictionary and then not being able to print
#in order without using sort and I played with some built in functins like filter,heap,item getters 


#-----2



#-----3

my_list = [67, 45, 2, 13, 1, 998]
my_list1 = [89, 23, 33, 45, 10, 12, 45, 45, 45]
your_list = []
your_list1 = []
while my_list:
    minimum = my_list[0]   
    for x in my_list: 
        if x < minimum:
            minimum = x
    your_list.append(minimum)
    my_list.remove(minimum)    
while my_list1 :
    minimum = my_list1 [0]   
    for x in my_list1 : 
        if x < minimum:
            minimum = x
    your_list1.append(minimum)
    my_list1 .remove(minimum)  
print('3: ', your_list)
print('3: ', your_list1)

#233 steps
# it iterates through each list and finds the lowest value which is the minimum and then compares
# the rest of the list. if nothing is found then that minimum number is put into the
# your_list and deletes that index(key and value) and then keeps iterating till the my list is
#completly been transfered to your list

#-----3



#----4
myList = [67, 45, 2, 13, 1, 998]
yourList = []
for i in range(len(myList)):
    a = min(myList)
    yourList.append(a)
    myList.remove(a)

print ('4: ', yourList)
#28 steps
# i thought this was the smoothest and fastest code with 28 steps
# it runs through the lenght of the list and looks for the smallest number then appends
# that value into the new yourlist  while removing what was transfered.

#----4

#----5

myList = [89, 23, 33, 45, 10, 12, 45, 45, 45] 
for i1, e1 in enumerate(myList):
   for i2, e2 in enumerate(myList):
      if e2 > e1:
         e1 = myList[i2]
         myList[i2] = myList[i1]
         myList[i1] = e1
print('5: ', myList)

#225
#enumerate what it does it takes my list and the two for statment and iterates
#myList compares the value in the if of e2 is greater then e1 and then keeps track
#of the larger value and then keeps iterating through the whole list comparing values.


#----5


#----6
my_list = [67, 45, 2, 13, 1, 998]
from itertools import permutations
for p in permutations(my_list):
     if all(i<=j for i,j in zip(p,p[1:])):
         print ('6: ', p)
         

# 0ver 1000 and program stopped this  is a clunky code and i am not sure but its a long running code
# i dont even know what this does it jumps around and its confusing other then that
# it works but the code checker stated its too long and it stopped after 1000 steps.

#----6






#----7

mylist = [67, 45, 2, 13, 1, 998]

n = 0
for z in mylist:
    n+=1
for i in range(n):
    for j in range(1, n-i):
        if mylist[j-1] > mylist[j]:
             (mylist[j-1], mylist[j]) = (mylist[j], mylist[j-1])
print('7: ', mylist)
#68
#starts interating thought the  list postition 0 and then rememebers the biggest number
#and  then selects the next index iterating the list comparing the value incrementing the diffence with the next index and then if the
# next number is bigger it slides the number to the right till it is in ascending order.
#my best guess thats what its doing.

#----7



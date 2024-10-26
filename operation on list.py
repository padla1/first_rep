numbers=[6,99,55,12,48,71,23,61,12,41,85,74,23,66,4]


#list length
print('list length =',len(numbers))

#first element
print('first element =', numbers[0])

#list slice from 4th to 7th element
print(numbers[4:7])

#maximum element
print('maximum element = ',max(numbers))

#minimum element
print('minimum element = ',min(numbers))

#sum of list element
print('sum of list element =',sum(numbers))

#list in reverse order
print(list(reversed(numbers)))


#print (list(sorted(numbers, reverse=True)))
print (list(sorted(numbers, reverse=False)))
print(list(sorted(numbers)))

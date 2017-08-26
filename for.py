# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 23:58:48 2017

@author: sdadh
"""

for letter in "python":
    print("letter is:", letter)
    
fruits=['banana','orange','mango']

for fruit in fruits:
    print("fruit is:",fruit)
    
    fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print ('Current fruit :', fruits[index])

for num in range(10,20):  #to iterate between 10 to 20
   for i in range(2,num): #to iterate on the factors of the number
      if num%i == 0:      #to determine the first factor
         j=num/i          #to calculate the second factor
         print ('%d equals %d * %d' % (num,i,j))
         break #to move to the next number, the #first FOR
   else:                  # else part of the loop
      print (num, 'is a prime number')
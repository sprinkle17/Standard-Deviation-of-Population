#Dalton sprinkle
#CS 120 02
#Final Project B
#Due: December 11th
#Turned in: 
#Program Description: This program will take the file 'Numbers.txt' and calculate the total of the numbers in the file then find the mean. Then the standard deviation of those numbers will be calculated and returned.
import math
numbers = open('numbers.txt')
contents = numbers.read()
splitted = contents.split()


def meanFunc():
  total = sum([int(num) for num in splitted])
  global totallinecount
  totallinecount = sum(1 for line in open("numbers.txt"))
  global mean
  mean = total/totallinecount
  print("The total is:",total)
  print("The mean is:",mean,"(Rounded to 3 decimals)")


def ALTNum():
  totals = 0
  for number in splitted:
    number = int(number)
    subtract = mean - number
    squared = (subtract**2)
    totals = totals + squared
    print(totals)
  divided = totals / totallinecount
  squareroot = math.sqrt(divided)
  print("The standard deviation of the population is:",squareroot)

meanFunc()
ALTNum()

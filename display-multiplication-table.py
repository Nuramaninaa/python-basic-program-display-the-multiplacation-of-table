#python program to display multiplication table

#input from user
n = int(input("Enter the number which user want for multiplication table : "))

#loop for 10 times
for i in range(1,13):
  print (n, i, '=', n*i)
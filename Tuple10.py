'''
 Write the program to count the number of times the given number (x) is present in the given tuple list and print it's factorial value without using factorial() method.
Sample Input:
1 2 3 4 1 5 1
1
Sample Output:
6
'''
input_values = input("Enter tuple values (separated by space): ")
values_tuple = tuple(map(int, input_values.split()))
x = int(input("Enter the number to count: "))
count_x = values_tuple.count(x)

factorial = 1
for i in range(2, count_x + 1):
    factorial *= i

print(factorial)

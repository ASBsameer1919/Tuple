'''
Write a program to get tuple elements in a single line separated by spaces and print the sum of the elements without using sum() method.
Sample Input:
10 20 30
Sample Output:
60
'''
lst=[]
n=int(input())
for i in range(0,n):
    ele=int(input())
    lst.append(ele)
e=tuple(lst)
t=sum(e)
print(t)

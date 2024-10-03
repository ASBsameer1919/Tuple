'''
 Write a program to get n number of tuple elements from the user in separate lines and print the sum of their values using predefined method.
Sample Input:
3
10
20
30
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

'''
Write a program to get n number of values from user in separate line and print the minimum value of the given tuple.
Sample Input:
3
20
30
10
Sample Output:
10
'''
lst=[]
n=int(input())
for i in range(0,n):
    ele=int(input())
    lst.append(ele)
e=tuple(lst)
t=min(e)
print(t)

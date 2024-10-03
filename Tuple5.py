'''
Write a program to get n number of tuple elements from the user in separate line and print the maximum value of the given values.
Sample Input:
3
20
10
30
Sample Output:
30
Ans
'''
lst=[]
n=int(input())
for i in range(0,n):
    ele=int(input())
    lst.append(ele)
e=tuple(lst)
t=max(e)
print(t)

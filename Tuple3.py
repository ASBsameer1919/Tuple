'''
Write a program to get the tuple elements in a single line separated by spaces and print the number of elements in the given tuple.
Sample Input:
10 20 30
Sample Output:
3
'''
lst=[]
n=int(input())
c=0
for i in range(0,n):
    ele=int(input())
    lst.append(ele)
    c=c+1
print(c)

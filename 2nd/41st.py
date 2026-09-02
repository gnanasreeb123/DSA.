n=int(input())
arr=list(map(int,input().split()))

k=int(input())
'''emp=[]
i=0
while i<k:
    emp.append(arr.pop())
    i+=1
emp.reverse()
for j in arr:
    emp.append(j)
print(emp)
'''
emp=arr[-k:]+arr[:-k]
print(emp)
    
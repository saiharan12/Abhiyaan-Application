#inputs taken
i=input()
#inputs split and put into a matrix
m,n =i.split()
m,n=int(m),int(n)
k = int(input())
li=[]
for i in range(m):
    t=input()
    t=t.split()
    #reformating from string to integers
    for c in range(len(t)): t[c]=int(t[c])
    li.append(t)

h=m-1
l=0

#running a binary search to find the row
while l<=h:
    mid=(h+l)//2

    if li[mid][0] < k:
        l = mid + 1

    elif li[mid][0] > k:
        h = mid - 1

    else:
        r=mid
        break

else:
    if li[mid][0] > k:
        r=mid-1
    else:
        r=mid

#running a binary search to find the element in the corresponding row
h=n-1
l=0

while l<=h:
    mid=(h+l)//2

    if li[r][mid] < k:
        l = mid + 1

    elif li[r][mid] > k:
        h = mid - 1

    else:
        print(True)
        print(str(r)+" "+str(mid))
        break
else:
    print(False)
   

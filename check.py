from math import *
#13
n=int(input())
gio =n//3600 #trong trường hợp n<3600 thì giờ bằng 0
n=n- gio *3600 #cập nhật lại giá trị của n
phut =n//60
n=n-phut *60
print("{:d} gio {:d} phut {:d} giay".format(gio,phut,n))
#14 nhập n và in ra các ước của n (không bao gồm n)
from math import *
n =int(input())
def uocj(n):
    if n==0:
        return 0
    a=[1]
    for i in range (2,isqrt(n)+1):
        if n%i==0:
            a.append(i)
            if i!= n//i:
                a.append(n//i)
    #nếu ở đây bao gồm cả n thì a.append (n)
    print(*(sorted(a)))
uocj(n)
#15 tương tự như 14 nếu bao gồm n thì cho a+1
from math import *
n=int(input())
def uoc(n):
    if n==0:
        return 0
    a=1
    for i in range (2,isqrt(n)+1):
        if n%i==0:
            a+=1
            if i!= n//i:
                a+=1
    print(a)
uoc(n)
#16 a, tính tổng 1 đến 2n, b tính tổng lẻ, c tính tổng chẵn cách dễ nhất và t sẽ làm
#thuật toán for đến chết :v
n=int(input())
tol=(n*2+1) *((n*2)//2)

tongle=tongchan=0
for i in range (1,n+1):
    if i%2==0:
        tongchan+=i
    else:
        tongle+=i
print(tol,tongle,tongchan)
#17 tính tổng ước nguyên tố của n (có n) , tổng các ước của n(không có n)
#tính tổng bình phương từ 1 đến n
from math import *
n=int(input())
def nt(n):
    if n < 2:
        return 0
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return 0
    return 1


def tonguoc(n):
    if n == 0:
        return 0
    s = 1
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            s += 1
            if i != n // i:
                s += n // i
    return s


def tongUocNT(n):
    s = 0
    if n < 2:
        return 0
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            if nt(i):
                s += i
            if i != n // i and nt(i):
                s += i
    if nt(n):
        return s + n
    return s


s = 1
for i in range(2, n + 1):
    s += i * i
print(tonguoc(n), tongUocNT(n), s)
#18
print(type(input()))
#19
n=int(input())
def kt(n):
    s=1
    for i in range (2,n+1):
        s+=i*i
    ss= (n*(n+1)*(2*n+1))/6
    return ss==s
if kt (n):
    print("YES")
else:
    print("NO")
#20 dùng thuật toán trâu
s=ss=0
n=int(input())
for i in range (1,n+1):
  s+=i*i*i
  ss+=i
print(s==(ss*ss))
#21 dùng sàng nguyên tố
from math import *
prim=[True]*(10**4+1)
prim[0]=prim[1]=False
for i in range (2,isqrt(10**4)+1):
    if prim[i]==True:
        for j in range (i*i,10**4+1,i):
            prim[j]=False
dem=0
for i in range (2,10**4 +1):
    if prim[i]:
        dem+=1
print(dem)
#22 dùng sàng số nguyên tố + tìm kiếm nhị phân
from math import*
n=int(input())
prim=[True]*(10**6 +1)
prim[0]=prim[1]=False
for i in range (2,isqrt(10**6)+1):
    if prim[i]==True:
        for j in range (i*i,10**6+1,i):
            prim[j]=False
prime=[i for i in range (2,10**6+1) if prim[i]]
def bin(a,l,r,x):
    res=-1
    while l<=r:
        m=(l+r)//2
        if a[m] >=x:
            res=m
            r=m-1
        else:
            l=m+1
    return prime[res]
print(bin(prime,0,len(prime)-1,n))
#23
from math import *
n=int(input())
def hh(n):
    if n<1:
        return 0
    s=1
    for i in range (2,isqrt(n)+1):
        if n%i==0:
            s+=i
            if i!=n//i:
                s+=n//i
    return s==n
if hh(n):
  print("YES")
else:
  print("NO")

#24 in ra số hoàn hảo từ 1 đến 10**4
from math import *
def hh(n):
    if n<1:
        return 0
    s=1
    for i in range (2,isqrt(n)+1):
        if n%i==0:
            s+=i
            if i!=n//i:
                s+=n//i
    return s==n
for i in range (1,10**4+1):
  if hh(i):
    print(i)
#25 sàng số nguyên tố :))
from math import*
prim=[True]*(10**4 +1)
prim[0]=prim[1]=False
for i in range (2,isqrt(10**4)+1):
    if prim[i]==True:
        for j in range (i*i,10**4+1,i):
            prim[j]=False
prime=[x for x in range (2,10**4+1) if prim[x]]
for i in range (1,len(prime)-1):
    if prime[i]-prime[i-1]==2:
        print(prime[i-1],prime[i])


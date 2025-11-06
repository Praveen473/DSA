# num = 9669
# res = num
# ans = num
# digits = list(str(num))   # ['9','9','6','3']
#
# for i in range(len(digits)-1):
#     for j in range(i+1, len(digits)):
#         # swap
#         digits[i], digits[j] = digits[j], digits[i]
#         new_num = int("".join(digits))
#         if new_num > ans:
#             ans = new_num
#         # swap back (to restore original for next loop)
#         digits[i], digits[j] = digits[j], digits[i]
# print(ans)
# a = int(input())
# r = []
#
# for i in range(a):
#     r.append(input().split())   # split into list
#
# for i in range(a):
#     print(r[i][2])   # pick the 3rd element (index 2)



# print(bin(10))
# print(bin(9))
# print(bin(10&9))


#___________________Practice
#vars
# class kk:
#     a=10
#     def __init__(self,b):
#         self.b=b
#     def call(d,c):
#         print(c)
#         print(kk.a)
#         print(d.b)
# cc=kk(3)
# cc.call(5)



# class kk:
#     def public(self,a):
#         self.a=a
#         print(a)
#     def _protected(self,b):
#         self.b=b
#         print(b)
#     def __private(self,c):
#         self.c=c
#         print(c)
#     def service(self):
#         self.public(10)
#         self.__private(12)
#         self._protected(11)
# class c(kk):
#     def __init__(self):
#         pass
#
# bb=c()
# bb._protected(123)
#
# # a=kk()
# # a.public(111)
# # a._protected(112)
# # a.service()
# # a.__private(113)

#
# class kk:
#     com="tata"
#     def __init__(self,c):
#         self.c=c
#     @classmethod
#     def classa(cls,new):
#         cls.com=new
#         print(cls.com)
#     @staticmethod
#     def stat(c):
#         print(c)
# cc=kk(1)
# cc.classa("ta")
# cc.stat("tat")

#
# class A:
#     a=10
#     def call(self,b):
#         self.b=20
# class B(A):
#     def call1(self):
#         super().call(5)
#         print(self.a,self.b)
# c=B()
# c.call1()

# a=10
# b=20
# print(a+b)
# c="A"
# d="ss"
# print(c+d)

# class test:
#     def method_overloading(a,b=None):#eventhough we are not declare self it take a as self ---------------------------------****************------------------------
#         print(b)
# def method(a,b=None):
#     print(b)
#
# a=test()
# a.method_overloading(10)#a value is self assign b=10
# method(10,2)

# class KK:
#     def call1(self,*a):
#         print(*a)
# c=KK()
# c.call1(10,20,30)

# class KK:
#     def hello(self,a,b=None):
#         if b is None:
#             print("None")
#         else:
#             print(a,b)
# a=KK()
# a.hello(10,20)
# a.hello(10)


# from abc import *
#
# class KK(ABC):
#     @abstractmethod
#     def show(self):
#         pass
# class b(KK):
#     def show(self):
#         print("S")
# c=b()
# c.show()
#
# from functools import *
# a=[1,2,3,4,5]
# c=(reduce(lambda x,y:x+y,a))
# print(c)
#


# class A:
#     def __init__(self):
#         print("SS")
# class B:
#     def __init__(self):
#         self.A=A()
# c=B()



# class too(Exception):
#     print("S")
#
# raise too("please")

#
# from threading import *
# def dis():
#     for i in range(10):
#         print(i)
# t=Thread(target=dis)
# t.start()
# for i in range(4):
#     print("main")


# from threading import *
# class Mythread(Thread):
#     def run(self):
#         for i in range(10):
#             print(i)
# t=Mythread()
# t.start()
# for i in range(4):
#     print("main")

# from threading import *
# import time
# I=Lock()
# def wish(name):
#     I.acquire()
#     for i in range(4):
#         print(name)
#         time.sleep(2)
#     I.release()
# t=Thread(target=wish("gokul",))
# t1=Thread(target=wish("goku",))

# import copy
# a=[1,23,4]
# c=copy.copy(a)
# c[0]=2
# print(a,c)


# a=[1,2,5,4,3]
# f=a[0]
# s=a[1]
# if f<s:
#     f,s=s,f
# for i in range(2,len(a)):
#     if a[i]>s:
#         if a[i]>f:
#             s=f
#             f=a[i]
#         else:
#             s=a[i]
# print(s)

# def factorial(n):
#     if n == 0 or n == 1:  # Base case
#         return 1
#     else:
#         return n * factorial(n - 1)
# print(factorial(5))

# prime=5
# s=0
# for i in range(2,prime//2):
#     if prime%i==0:
#         s=1
#         break
# if s==0:
#     print("prime")
# else: print("not prime")

# prime = 50
# a=[]
# s=0
# for i in range(2,prime):
#     s=0
#     for j in range(2,i):
#         if i%j==0:
#             s=1
#             break
#     if s==0:
#         a.append(i)
# print(*a)


# # Create a list with "T" values
# a = ["T"] * prime
#
# # Mark non-primes as "f"
# for i in range(2, int(prime ** 0.5) + 1):  # Only need to go up to √prime
#     if a[i] == "T":
#         for j in range(i * i, prime, i):
#             a[j] = "f"
#
# # Print prime numbers
# for i in range(2, prime):
#     if a[i] == "T":
#         print(i, end=" ")

#
# a="string birth day"
# c=a.split()
# d=""
# print(c[::-1])
# for i in c:
#     print(i)
#     d=d+"".join(i[::-1])
#     d=d+" "
# print(d)

# a=1120
# res=""
# l=len(str(a))
# while l>0:
#     c=a%10
#     res+=str(c)
#     a=a//10
#     l-=1
#
# print(res)

# map={'}':'{',')':'(',']':'['}
# inp="([{}])"
# s=[]
# for i in inp:
#     if i in map.values():
#         s.append(i)
#     else:
#         if len(s)>0 and s[-1]!=map[i]:
#             print("not valid")
#         s.pop()


# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.nxt=None
# class LL:
#     def creat(self,arr):
#         head=Node(arr[0])
#         curr=head
#         for i in arr[1:]:
#             curr.nxt=Node(i)
#             curr=curr.nxt
#         return head
#     def print1(self,arr):
#         while(arr!=None):
#             print(arr.data)
#             arr=arr.nxt
#     def rev(self,arr):
#         prev=None
#         curr=arr
#         while(curr!=None):
#             next_node=curr.nxt
#             curr.nxt=prev
#             prev=curr
#             curr=next_node
#         return prev
#
#
#
# a=LL()
# res=a.creat([1,2,3,4,5])
# a.print1(res)
# res1=a.rev(res)
# a.print1(res1)


# class tree:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None
# class buil:
#     def creat(self,root,key):
#         if root is None:
#             return tree(key)
#         if root.data>key:
#             root.left=self.creat(root.left,key)
#         else:
#             root.right=self.creat(root.right,key)
#         return root
#     def print1(self,arr):
#         if arr:
#             print(arr.data)
#             self.print1(arr.left)
#             self.print1(arr.right)
# c=buil()
# a=[4,3,2,6,1,2]
# root=None
# for i in a:
#     root=c.creat(root,i)
# c.print1(root)


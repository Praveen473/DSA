# print(type(float('inf')))
#
# a=float('-inf')
# b=10
# if b>a:
#     print(b)
#
# c="listen"
# d="silent"
# if sorted(c)==sorted(d):
#     print("s")
# a=[5, 7, 2,8, 9, 1]
# first=a[0]
# second=a[1]
# if first<second:
#     first,second=second,first
# for i in a:
#     if second<i:
#         if first<i:
#             second=first
#             first=i
#         else:
#             second=i
# print(second)
from functools import reduce

# a=[1,2,4,7,8,9,11,13]
# t=9
# l=0
# r=len(a)-1
# while l<r:
#     mid=(l+r)//2
#     if a[mid]==t:
#         print("yes")
#         break
#     elif a[mid]>t:
#         r = mid - 1
#     else:
#         l = mid + 1

# dict={}
# a="hyvee"
# for i in a:
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i]=1
# print(dict)

# def is_balanced(expr):
#     stack=[]
#     match={')':'(',']':'[','}':'{'}
#     for ch in expr:
#         if ch in '([{':
#             stack.append(ch)
#         elif ch in ')]}':
#             if not stack or stack.pop()!=match[ch]:
#                 print("false")
#     print("true")
#
# print(is_balanced("{[()]}"))
#
# s="hyvee"
# rev=""
# for ch in s:
#     rev=ch+rev
# print(rev)

# a=[1,2,4,5]
# b=[3,4,6]
# out=a+b
# out.sort()
# print(out)


# class Node:
#     def __init__(self,val):
#         self.val=val
#         self.next=None
# class ll:
#     def create(self,a):
#         root=Node(a[0])
#         curr=root
#         for i in a[1:]:
#             curr.next=Node(i)
#             curr=curr.next
#         return root
#     def print1(self,root):
#         while root != None:
#             print(root.val)
#             root = root.next
#     def rev(self,root):
#         prev=None
#         curr=root
#         while curr:
#             newNode=curr.next
#             curr.next=prev
#             prev=curr
#             curr=newNode
#         return prev
#
#     def cyc(self,root):
#         slow=fast=root
#         while fast and fast.next:
#             slow=slow.next
#             fast=fast.next.next
#
# call=ll()
# a=[1,2,3,4,5]
# res=call.create(a)
# call.print1(res)
# res1=call.rev(res)
# call.print1(res1)



# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
# class BST:
#     # Insert a value into the BST
#     def insert(self, root, key):
#         if root is None:
#             return Node(key)
#         if key > root.data:
#             root.right=self.insert(root.right,key)
#         elif key<root.data:
#             root.left = self.insert(root.left, key)
#         return root
#
#     # In-order traversal (prints sorted elements)
#     def inorder(self, root):
#         if root:
#             self.inorder(root.left)
#             print(root.data, end=" ")
#             self.inorder(root.right)
#
# # Main code
# arr = [1,2,5,4,3]#list(map(int, input("Enter elements of the array separated by space: ").split()))
# bst = BST()
# root = None
#
# # Insert each element into BST
# for num in arr:
#     root = bst.insert(root, num)
#
# print("In-order Traversal of BST:")
# bst.inorder(root)


#####__________________________###########################

# res = ["compaign c 4", "compaign d 1", "compaign a 4", "compaign p 0", "compaign e 7", "compaign f 3"]
# res1=sorted(res,key=lambda s:(-(int(s.split()[2])),-ord(s.split()[1])))   #-ord(letter) makes letters descending (since ord('a')=97, ord('z')=122)
# #res1 = sorted(res, key=lambda s: (int(s.split()[2]), s.split()[1]), reverse=True) #both descending
# print(res1)
#
# data = {"apple": 3, "banana": 1, "cherry": 5, "date": 2}
# asc_keys = dict(sorted(data.items(), key=lambda x: x[0]))
# print(asc_keys)  # {'apple': 3, 'banana': 1, 'cherry': 5, 'date': 2}
#
# desc_keys = dict(sorted(data.items(), key=lambda x: x[0], reverse=True))
# print(desc_keys)  # {'date': 2, 'cherry': 5, 'banana': 1, 'apple': 3}
#
# asc_values = dict(sorted(data.items(), key=lambda x: x[1]))
# print(asc_values)  # {'banana': 1, 'date': 2, 'apple': 3, 'cherry': 5}
#
# desc_values = dict(sorted(data.items(), key=lambda x: x[1], reverse=True))
# print(desc_values)  # {'cherry': 5, 'apple': 3, 'date': 2, 'banana': 1}
#
# combo = dict(sorted(data.items(), key=lambda x: (x[1], x[0])))
# print(combo)# {'banana': 1, 'date': 2, 'apple': 3, 'cherry': 5}

#combination
# def val(a,t):
#     def call(a,t,res,pas,used):
#         if sum(res)==t:
#             pas.append(res)
#             return
#         if sum(res)>t:
#             return
#         for i in range(len(a)):
#             if not used[i]:
#                 used[i]=True
#                 call(a,t,res+[a[i]], pas,used)
#                 used[i]=False
#     pas=[]
#     used=[False]*len(a)
#     call(a, t, [],pas,used)
#     return pas
# a = [1, 2, 3, 4, 5]
# t = 4
# c=val(a,t)
# print(c)
#
#
# #permutation
# def call(arr, tar, res, index):
#     current_sum = sum(res)
#     if current_sum > tar:
#         return
#     if current_sum == tar:
#         print(res)
#         return
#     #without loop
#     if index >= len(arr):
#         return
#     #for i in range(index, len(arr)):
#     call(arr, tar, res + [arr[index]], index + 1)
#     call(arr, tar, res, index + 1)
# a=[1,2,3,4,5]
# t=4
# index=0
# call(a,t,[],0)
#
# #combinations with reuse
# def val(a, t):
#     def call(start, res, pas):
#         if sum(res) == t:
#             pas.append(res[:])
#             return
#         if sum(res) > t:
#             return
#
#         for i in range(start, len(a)):
#             # allow reuse by passing i (not i+1)
#             call(i, res + [a[i]], pas)
#
#     pas = []
#     call(0, [], pas)
#     return pas
#
#
# a = [1, 2, 3, 4]
# t = 4
# c = val(a, t)
# print(c)


# def call(arr, tar, res, index):
#     current_sum = sum(res)
#     if current_sum > tar:
#         return
#     if current_sum == tar:
#         print(res)
#         return
#     for i in range(index, len(arr)):
#         #call(arr, tar, res + [arr[i]], index + 1) #[1, 3][2, 2][4]
#         call(arr, tar, res + [arr[i]], i + 1)  # [1, 3][4]  to avoid reuse
#  a = [1, 2, 3, 4]
#  t = 4
#call(a,t,[],0)

# def call(arr, tar, res, index,res1):
#     current_sum = sum(res)
#     if current_sum > tar:
#         return
#     if current_sum == tar:
#         res1.append(res)
#         #print(res)
#         return
#     for i in range(index, len(arr)):
#         call(arr, tar, res + [arr[i]],i,res1) #duplicates
#         # call(arr, tar, res + [arr[i]], i + 1,res1)  #no duplicates
# a=[20,10,5,1]
# t=70
# res1=[]
# call(a,t,[],0,res1)
# print(res1)
# z=min(len(i) for i in res1)
# z1=[i for i in res1 if len(i)==z]
# print(z1,z)



# star --- pyramid
# x=[0,1,259]
# b=bytes(x)
# print(*b)
# n = int(input("Enter number of rows:"))
# for i in range(1,n+1):
#     print(" " * (n-i),end="")
#     print("* "*i)
#
# n=list(map(int,input().split()))
# print(*n)
# from functools import *
# l=[1,2,3,4,5]
# c=reduce(lambda x,y:x+y,l)
# print(c)
# def square(val):
#     if val%2==0:
#         return val
# a=[1,2,3,4,5]
# print(list(filter(square,a)))#[2,4]
# # print(list(square(a)))#error
# print(list(map(square,a)))
# class kk:
#     x=10
#     def call(self,k):
#         res=10
#         self.y=k
#         print(kk.x,self.y,res)
# a=kk()
# a.call(12)
# a=10
# _b=20
# __c=30
# print(a,_b,__c)

# class KK:
#     def public1(self):
#         print("public")
#     def _protected(self):
#         print("protected")
#     def __private(self):
#         print("private")
#     def private(self):
#         self.__private()
# a=KK()
# a.public1()
# a._protected()
# a.private()
#
# class acc:
#     def __init__(self,owner,balance):
#         self.owner=owner
#         self.__balance=balance
#     def get_balance(self):
#         return self.__balance
#     def depos(self,amt):
#         if amt>0:
#             self.__balance+=amt
#         else:
#             print("invalid")
# ac=acc("alice",1000)
# print(ac.get_balance())

# class kk:
#     @classmethod
#     def cl(cls,s):
#         cls.val=s
#         print(cls.val)
#
#     @staticmethod
#     def c2(a,b):
#         return a+b
# a=kk()
# a.cl(10)
# print(a.c2(10,20))

# class a:
#     x=10
#     def kk(self):
#         self.res=10
# class b(a):
#     def val(self):
#         print(self.x)
#         self.kk()
#         print(self.res)
#
# c=b()
# c.val()

# class cc:
#     def cal(self,name=None):
#         if name :
#             print(name)
#         else:
#             print("hello")
# a=cc()
# a.cal()
# a.cal("ram")


# from abc import *
# class kk:
#     @abstractmethod
#     def ss(self):
#         print("S")
# a=kk()
# a.ss()

# from abc import *
# class kk(ABC):
#     @abstractmethod
#     def ss(self):
#         pass
# class c(kk):
#     def ss(self):
#         print("ss")
# a=c()
# a.ss()
class KK(Exception):
    def __init__(self, msg):
        self.msg = msg

def cc(x):
    if x == 10:
        raise KK("Value cannot be 10")

try:
    cc(10)
except KK as e:
    print("Custom Exception Occurred:", e)



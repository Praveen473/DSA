#odd even inorder rotation effective
# a = [1, 2, 3, 6, 5]
# even_index = 0
# for i in range(len(a)):
#     if a[i] % 2 != 0:
#         # Find the next even number after index i
#         for j in range(i + 1, len(a)):
#             if a[j] % 2 == 0:
#                 a[i], a[j] = a[j], a[i]
#                 break
# print(*a)#shorthand
#__________________________________________________________________________________________________________________
#second largest
# a=[1,2,3,4,0,7,9,2]
# fir=a[0]
# sec=a[1]
# for i in range(2,len(a)-1):
#     if a[i]<sec:
#         if a[i]<fir:
#             sec=fir
#             fir=a[i]
#         else: sec=a[i]
# print(fir,sec)
#__________________________________________________________________________________________________________________
#two sum
# def twoSum(nums, target):
#     num_map = {}  # Step 1: Create an empty dictionary to store number -> index
#
#     for i, num in enumerate(nums):  # Step 2: Loop through the list
#         complement = target - num  # Step 3: Calculate what number we need to reach the target
#
#         if complement in num_map:  # Step 4: Check if that number is already in the dictionary
#             return [num_map[complement], i]  # Step 5: If yes, return the stored index and current index
#
#         num_map[num] = i  # Step 6: Else, store the current number with its index in the dictionary
from operator import index
from tabnanny import check
from venv import create

from django.db.models.fields import return_None
from django.template.defaultfilters import title


#______________________________________________________________________________________

# def find_pairs(arr, target):
#     seen = set()   #___________________________________Important___________________________________________________
#     for num in arr:
#         if target - num in seen:
#             print((num, target - num))
#         seen.add(num)
#
# find_pairs([3, 7, 5, 1, 9, 2, 8], 10)

#_________________________________________________________________________________________________________
#__
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class ll:
#     def creating(self,head):
#         n=Node(head[0])
#         curr=n
#         for i in head[1:]:
#             curr.next=Node(i)
#             curr=curr.next
#         return n
#     def printll(self,head):
#         while head!=None:
#             print(head.data)
#             head=head.next
#
#     def reverse(self,curr):
#         prev=None
#         while curr:
#             nextnode=curr.next
#             curr.next=prev
#             prev=curr
#             curr=nextnode
#         return prev
# l=ll()
# a=[1,4,3,5]
# c=l.creating(a)
# l.printll(c)
# d=l.reverse(c)
# l.printll(d)

#______________________________________________dict__________________________________________________________________
#
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

#________________________________________________________________________________________________________________

# res = ["compaign p1 4", "compaign 4", "compaign p1 4", "compaign p0 7"]
#
# def get_p_value(entry):
#     parts = entry.split()
#     print(parts)
#     for part in parts:
#         if part.startswith('p') and part[1:].isdigit():
#             return int(part[1:])  # Extract number after 'p'
#     return float('inf')  # If no pN is found, put it at the end
#
# sorted_res = sorted(res, key=get_p_value)
#
# print(sorted_res)
#________________________________________________________________________________________________________________

#---------------------logic---------------------------
# res = ["compaign p1 4", "compaign 4", "compaign p1 4", "compaign p1 7", "compaign p0 7", "compaign 3"]
#
# def call(arr, work):
#     count_dict = {}
#     other_total = 0
#     for i in arr:
#         pat=i.split()
#         if len(pat)==3:
#             pt=pat[1]
#             time=int(pat[2])
#             count_dict[pt]=count_dict.get[pt,0]+time
#         elif len(pat)==2:
#             other_total+=int(pat[1])
#             count_dict["non"]=other_total
#
#     # Sort dictionary by key
#     for key in sorted(count_dict):
#         print(f"{key}: {count_dict[key]}")
#
# call(res, 6)

#------------------------------------Casa Retail AI-------------------------------------------------
# s="12233"
# dict={}
# seen=set()
# bool=True
# for i in range(len(s)-1):
#     if s[i] not in seen:
#         if s[i]==s[i+1]:
#             bool=False
#             dict[s[i]]=dict.get(s[i],1)+1
#         else:
#             if bool==True:
#                 dict[s[i]]=1
#             seen.add(s[i])
# print(dict)
#------------------------------------Casa Retail AI-------------------------------------------------
# nums=38
# print(str(nums))
# num = 38
# c=str(num)
# while num:
#     count = 0
#     for i in c:
#         print(i)
#         count += int(i)
#         print(count)
#     c = str(count)
#     if len(c)==1:
#         break
# print(count)

#------------------------------------Casa Retail AI-------------------------------------------------

#----------------------------------datagrokr----------------------------
# n = int(input())  # 3
# rows = []
# for _ in range(n):
#     parts = input().split()
#     rows.append([parts[0], int(parts[1]), int(parts[2])])#----------------------------------datagrokr----------------------------
#     print(*rows)
# # Access 45
# print(rows[0][2])   # Output: 45

# s="dfdfdf adss"
# d=''.join(s.split())
# print(type(d))

# s=["compaign p1 4", "compaign 4", "compaign p1 4", "compaign p1 7", "compaign p0 7", "compaign 3"]#------------------------datagrokr------------
# print(s[0])
# for i in s:
#     part=i.split()
#     print(part[0])

#----------------------------------datagrokr----------------------------------------------------datagrokr------------
# data = {}
# n = int(input())   # 3
#
# for _ in range(n):
#     parts = input().split()
#     key = parts[0]       # "app"
#     #values = list(map(int, parts[1:]))  # [3, 45]
#     data[key] = parts[1:]
#
# # Access 45
# print(data["awq"][1])   # Output: 45
#----------------------------------datagrokr----------------------------


#--------------------------------cariad----------------------------cariad
# class Book:
#     def __init__(self,title,gen,rat):
#         self.title=title
#         self.gen=gen
#         self.rat=rat
#     def __str__(self):  # this makes print(object) readable
#         return f"{self.title}, {self.gen}, {self.rat}"
# class lib:
#     def __init__(self):
#         self.book=[]
#     def addbook(self,book):
#         self.book.append(book)
#         for i in self.book:#--------------------------------imp----------------------------imp
#             print(i)
#     def top(self,x):
#         res=sorted(self.book,key=lambda b: (b.title,b.rat))
#         return res[:x]
#     # def rec(self,var):
#     #     return
# l=lib()
# n=int(input())
# for i in range(n):
#     title,gen,rat=input().split(',')
#     l.addbook(Book(title,gen,float(rat)))
# inp=int(input())
# top1=l.top(inp)
# for i in top1:
#     print(f"{i.title} value is {i.rat}")



#--------------------------------cariad----------------------------cariad

# #------------------------------------------murfai----------------------------------
# def val(a,t):
#     def call(a,t,res,start,pas):
#         if sum(res)==t:
#             pas.append(res)
#             return
#         if sum(res)>t:
#             return
#         for i in range(start,len(a)):
#             call(a,t,res+[a[i]],start+1, pas)
#     pas=[]
#     call(a, t, [], 0,pas)
#     return pas
# a = [1, 2, 3, 4, 5]
# t = 4
# c=val(a,t)
# print(c)
# #------------------------------------------murfai----------------------------------


# import requests
#
#
# def get_highest_rank(api_url, name):
#     # 1. Fetch JSON from API
#     response = requests.get(api_url)
#     data = response.json()
#
#     # Example JSON:
#     # [
#     #   {"name": "Alice", "rank": 3, "score": 95},
#     #   {"name": "Bob", "rank": 1, "score": 88},
#     #   {"name": "Alice", "rank": 2, "score": 99}
#     # ]
#
#     # 2. Filter all records for the given name
#     records = [item for item in data if item["name"].lower() == name.lower()]
#
#     if not records:
#         return f"{name} not found!"
#
#     # 3. Find record with minimum rank
#     best_record = min(records, key=lambda x: x["rank"])
#
#     return best_record
#
#
# # Example usage
# api_url = "https://example.com/api/rankings"  # replace with actual URL
# name = input("Enter name: ")
# result = get_highest_rank(api_url, name)
#
# print("Best record:", result)
# #------------------------------------------murfai----------------------------------

#------------------------------------------hyvee----------------------------------
# a = {"a": 5, "b": 1}
# b = {"a": 1, "b": 1}
# output = {}
# for key in a:
#     output[key] = a[key] - b[key] #"b.get(key, 0)"
# #output = {key: a.get(key, 0) - b.get(key, 0) for key in a}
# print(output)
# nums = [0,0,0,2,0,0]
# res=[0]
# n=1
# count=0
# while n<len(nums):
#     arr=[]
#     for i in range(len(nums)):
#         for j in range(i,i+n):
#             if j<len(nums):
#                 arr.append(nums[j])
#                 if arr==res:
#                     count+=1
#         arr=[]
#     n+=1
#     res.append(0)
# print(count)
#------------------------------------------hyvee----------------------------------
#------------------------------------------poorni open data ----------------------------------

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
#------------------------------------------poorni open data ----------------------------------
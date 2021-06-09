#!/usr/bin/env python
# coding: utf-8

# In[1]:


##Program to check whether the person is available for vote or not
a=int(input("enter age of the person")) 
if a>=18:
    print("the person is eligible to vote")
else:
    print("the person is not eligible to vote")


# In[2]:


##Program to check whether a number is positive or not
a=int(input("Enter any number:"))
if a>=0:
    print("The given number is positive number")
else:
    print("the given number is negative number")


# In[3]:


##program to check the given number is even or odd if it's even check which is divisible by 4 or not

a = int(input(" Enter number: "))

if (a % 2) ==0 :
    if (a % 4) ==0:
        print("given number is even and divisible by 4 ")
    else:
        print("given number is even and not divisible by 4 ")
else:
    print("given number is odd")


# In[4]:


a = int(input("Enter percantage obatained by the student"))
if a>=92:
    print("distinction")
elif a>=50:
    print("pass")
else:
    print("fail")


# In[5]:


# program to check if year is a leap year or not

a = int(input("Enter year here "))

if (a % 4) == 0:
   if (a % 100) == 0:
       if (a % 400) == 0:
           print(" is a leap year")
       else:
           print(" is not a leap year")
   else:
       print("is a leap year")
else:
   print(" is not a leap year")


# In[ ]:





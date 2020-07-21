#!/usr/bin/env python
# coding: utf-8

# # backslash \

# In[1]:


print("hello       world")


# backslash "\" is used for continuity.

# In[3]:


print("hello \n world")


# \n- escape sequence;moves the cursor to next line

# In[4]:


print("python\'s world'")


# here, \ signifies that the code is in continuity and occurence of ' is a part of the string and not the end of string.

# # triple quotes

# In[ ]:


print("""hello 
how 
are 
you""")


# """""""- to write the text as it is, for multiline comments
# 

# # variables and assignment 

# In[1]:


a=12
print(a)


# varible's  name can contain alphanumeric characters and underscore only and cannot start with numbers.
# "=" is an assignment operator and assigns the value to variable

# # formatting.

# In[5]:


name="arushi"
marks=90
age=20
print("the name is ",name," age is ",age ," marks are ",marks)


# In[8]:


print("the name is %s and age is %d and marks are %d"%(name,age,marks))


# In[9]:


print("the name is %3s and age is %5d and marks are %3d"%(name,age,marks))
# %3s signifies that name will be printed after 3 spaces


# In[4]:


name="rahul"
age=23
marks=36.8947
print("the name is %s and age is %d and marks are %3.2f"%(name,age,marks))
#.2f signifies the digits required after the decimal.


# # arithmetic operators
# 

# In[10]:


a=10
b=20
print(a+b) #addition
print(a-b) #subtraction
print(a*b) #multiplication
print(a/b) #division (int/int=float)
print(a//b) #floor division
print(a%b) #modulus
print(5**3) #exponentiation


# # assignment operators

# In[15]:


a=10
b=3
a+=b #a=a+b
print(a)
a-=b #a=a-b
print(a)
a*=b #a=a*b
print(a)
a/=b #a=a/b
print(a)


# # comparison operators

# In[16]:


a=12
b=13
print(a>b) #greater than
print(a<b) #lesser than
print(a==b) #equals to
print(a>=b) #greater than or equals to
print(a<=b) #lesser than or equals to
print(a!=b) #not equals to


# # logical operators

# In[17]:


print(2>3 and 4<5) #returns true only if both conditions are true


# In[18]:


print(6<7 or 9>0) #returns true even if one of the conditions is true


# In[19]:


print(not(3>6)) #inverts the actual result


# # identity operators

# In[20]:


a=12
b=12
print(a is b)  


# In[21]:


a=22
b=12
print(a is b)


# In[22]:


a="arushi"
b="arushi"
print( a is not b)


# In[23]:


a=257
b=257
print(a is b) #returns true only if both numbers are same and lie in the range -5 to 256


# In[24]:


a=1.3
b=1.3
print(a is b) #doesnt work for floating point values


# # membership operators

# In[26]:


#checks if the given substring is a part of actual string or not
a="hello world! lets learn python"
print("hello" in a)  #returns true if a given substring is in the actual string
print("world" not in a) #returns true if given substring is not in actual string


# # bitwise operators

# In[29]:


a=240
b=1
print(a&b)
print(a|b)
print(~a)


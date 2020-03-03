#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


# In[51]:


class Tree:
    def __init__(self):
        self.head = None
    def append(self,value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.head.next = self.head
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = newNode
            newNode.next = self.head
    def prepend(self,value):
        newNode = Node(value)
        if not self.head:
            self.head = newNode
            self.head.next = self.head
        else:
            newNode.next = self.head.next
            self.head.next = newNode
    def display(self):
        cur = self.head
        while cur.next!= self.head:
            print(cur.value)
            cur = cur.next
            
            


# In[52]:


del q


# In[54]:


q = Tree()


# In[55]:


q.prepend(4)


# In[66]:


q.display()


# In[65]:


q.prepend(10)


# In[ ]:





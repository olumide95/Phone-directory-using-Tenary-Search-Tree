# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 14:30:05 2018

@author: Olumideolu
"""
from tstnode import Node
class TST(object):
    
    def __init__(self):
        self.root = None
        
    def insert(self,key,value): ##insert key value pair {olumide,08148731745}
        
        self.root = self.insert_item(self.root,key,value,0) 
        
    def insert_item(self,node,key,value,index):
        
        data = key[index]
        if node is None: node = Node(data) 
        
        if data < node.character:
            node.left = self.insert_item(node.left,key,value,index)
        
        elif  data > node.character:
            node.right = self.insert_item(node.right,key,value,index)
            
        elif  index < len(key)-1:
            node.middle = self.insert_item(node.middle,key,value,index+1)
            
        else: node.value = value
        
        return node
    
    def get(self,key):
        
        node = self.root
        if node is None: return None
        
        node =  self.get_Item(self.root,key,0)
        
        return node is not None and node.value or None
    
    
    def get_Item(self,node,key,index):
        
        data  = key[index]
        
        if node is None: return None
        if data < node.character :
            return self.get_Item(node.left,key,index)
        
        if data > node.character:
           return self.get_Item(node.right, key,index)
       
        if index < len(key)-1:
           return self.get_Item(node.middle,key,index+1)
        else: return node
    
    def getPrefixHead(self,prefix):
        
        node =  self.get_Item(self.root,prefix,0)
        
        if node is not None: return node
        else: return None
    
    
    def auto_suggest(self,prefix):
        
        node = self.getPrefixHead(prefix)
        
        if node is not None: 
            if node.value is not 0:
                print(prefix)
            self.get_suggest(prefix,node.middle)
        else:  
            print("No suggestions Found") 
            return 
        
    def get_suggest(self,prefix,node,suggestion=""):
        
        if node is not None:
            self.get_suggest(prefix,node.left,suggestion)
            
            suggestion+= node.character
            
            if node.value is not 0:
                
                print(prefix+suggestion)
            
            self.get_suggest(prefix,node.middle,suggestion)
            
            
            self.get_suggest(prefix,node.right,suggestion)
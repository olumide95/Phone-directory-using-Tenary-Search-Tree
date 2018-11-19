# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 14:27:13 2018

@author: Olumideolu
"""

class Node(object):
    
    def __init__ (self,data):
        self.character = data
        self.left = None
        self.right = None
        self.middle = None
        self.value = 0
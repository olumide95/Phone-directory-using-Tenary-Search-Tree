# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 18:01:35 2018

@author: Olumideolu
"""

from TenarySearchTree import TST

        
tst = TST()
##insert Contacts
tst.insert('Olumide','08148731745')
tst.insert('Olumide olu','08148731745')
tst.insert('Olamide','08148731746')


#get contacts
tst.get('Olamide')

##auto suggest
prefix = 'Ol'
tst.auto_suggest(prefix)

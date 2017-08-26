# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 23:07:56 2017

@author: sdadh
"""

import webbrowser
import time
total_break=3
break_count=0
while(break_count<total_break):
  time.sleep(10)
  webbrowser.open('http://google.com')
  break_count=break_count+1
  print(time.ctime)
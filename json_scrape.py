# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 11:06:43 2017

@author: jrbrad
"""

import requests

my_wm_username = 'gvbrei'
search_url = 'http://buckets.peterbeshai.com/api/?player=201939&season=2015'
response = requests.get(search_url,'lxml')
 

numJumpShotsAttempt = 0
numJumpShotsMade = 0
percJumpShotMade = 0.0

# Write your program here to populate the appropriate variables
#EVENT_TYPE can be made shot, missed shot
#ACTION_TYPE can be "jump shot" 
#count the number of "made shots"
#count the number of made shots that are jump shots 
#calculate percentage of jump shots that were made shots
#make sure your numbers are floats

for shots in response.json():
    if shots['ACTION_TYPE'] == 'Jump Shot':
        numJumpShotsAttempt +=1
        if shots['EVENT_TYPE'] == 'Made Shot':
           numJumpShotsMade +=1

percJumpShotMade = float(numJumpShotsMade)/numJumpShotsAttempt      
    
    
        
        
            
        
    #puts into dictionary format




print my_wm_username
print numJumpShotsAttempt
print numJumpShotsMade
print percJumpShotMade

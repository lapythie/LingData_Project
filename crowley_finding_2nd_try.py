##go through attribute_errors.json
##pick indices of works that API previously failed to fetch
##check if a work has crowley as character
##if yes, add the work index to the list
##dump the list to json

import os
import json
from ao3 import AO3
api = AO3()

## directories with only tv fandom tag works
## and book fandom works respectively
path = '.'
character_name = 'Crowley'
caught_filename = 'crowley_works_2nd_try.json'
missed_filename = 'attribute_errors.json'

## list of indices of works featuring Crowley as strings
index_list = []

##lists of indices of works that API failed to connect with
with open(missed_filename, 'r', encoding='utf-8') as f:
    indices2check = json.load(f)

error_list = []

for work_index in indices2check:
##            some works can be already deleted
    try:
        work = api.work(id=work_index)
    except:
        error_list.append(work_index)
        
    try:
##                work.characters returns a list of characters
##                then we check if Crowley's name is mentioned
##                assume there may be different ways to tag him
        for character in work.characters:
            if character_name in character:
                index_list.append(work_index)
                continue
    except:
        pass
    
    if len(index_list)%100 == 0:
        print ('Works caught: ', len(index_list))

with open(caught_filename, 'w', encoding='utf-8') as f:
    json.dump(index_list, f)
with open(missed_filename, 'w', encoding='utf-8') as f:
    json.dump(error_list, f)
                
                
    

##go through both parts of the ao3 good omens corpus
##pick names of the files
##check if a work has crowley as character
##if yes, add the work index to the list
##dump the list to json

import os
import json
from ao3 import AO3
api = AO3()

## directories with only tv fandom tag works
## and book fandom works respectively
paths = ['tv_works', 'works']
character_name = 'Crowley'
ext = '.txt'
caught_filename = 'crowley_works.json'
missed_filename = 'attribute_errors.json'

## list of indices of works featuring Crowley as strings
index_list = []
##list of indices of works that API failed to connect with
error_list = []
for path in paths:
    for root, dirname, files in os.walk(path):
##        print ('Total files: ', len(files))
        for filename in files:
            
            work_index = filename.strip(ext)
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
            
##            if len(index_list)%100 == 0:
##                print ('Works caught: ', len(index_list))

with open(caught_filename, 'w', encoding='utf-8') as f:
    json.dump(index_list, f)
with open(missed_filename, 'w', encoding='utf-8') as f:
    json.dump(error_list, f)

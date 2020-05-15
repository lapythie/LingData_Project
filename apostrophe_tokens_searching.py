##go through texts of works featuring Crowley
##split a text to tokens
##check if there is apostrophe present in the token
##strip token of punctuation (leave apostrophe)
##collect a list of tokens with apostrophe stripped of punctuation
##map a counter of the tokens to the path where they were collected
##dump the dict to json

import os
import json
from collections import Counter
punctuation = '!"#$%&()*+,-./:;<=>?@[\]^_`{|}~«»—–…“”‘'

## directories with only tv fandom tag works
## and book fandom works respectively
paths = ['tv_works', 'works']
character_name = 'Crowley'
ext = '.txt'
caught_filename = 'crowley_works.json'
apo = "'"

## set of indices of works featuring Crowley as strings
with open(caught_filename, 'r', encoding='utf-8') as f:
    index_set = set(json.load(f))
    print ('Total indices: ', len(index_set))
    
tokens_dict = {}
output_filename = 'path_counter_dict.json'

for path in paths:
    for root, dirname, files in os.walk(path):
        for filename in files:
            if filename.strip(ext) in index_set:
                work_path = '{}/{}'.format(path, filename)
                with open (work_path, 'r', encoding='utf-8') as f:
                    work_tokens = f.read().split()
                apos = [token.strip(punctuation) for token in work_tokens if apo in token]
                tokens_dict.update({work_path:Counter(apos)})

            if len(tokens_dict)%100 == 0:
                print ('Works searched: ', len(tokens_dict))

with open(output_filename, 'w', encoding='utf-8') as f:
    json.dump(tokens_dict, f)

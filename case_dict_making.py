##go through texts of works featuring Crowley
##split a text to tokens
##check if there is apostrophe present in the token
##strip token of punctuation (leave apostrophe)
##collect a list of tokens with apostrophe stripped of punctuation
##map a counter of the tokens to the path where they were collected
##sort out single possessives and tokens that include punctuation
##dump the dict to json

import json
import re
from collections import Counter
punct_set = set('!"#$%&()*+,-./:;<=>?@[\]^_`{|}~«»…“”‘—–-')


##with open(output_filename, 'w', encoding='utf-8') as f:
##    json.dump(tokens_dict, f)

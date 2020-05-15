##go through path_counter_dict.json
##it's a dict that maps a Counter object of tokens (value)
##to path to the file where the tokens came from

##check if there is apostrophe present in the token
##strip token of punctuation (leave apostrophe)
##collect a list of tokens with apostrophe stripped of punctuation
##map a counter of the tokens to the path where they were collected
##sort out single possessives and tokens that include punctuation
##dump the dict to json

import json
import re
from collections import Counter

##same string like before but without hyphen-like symbols
punct_set = set('!"#$%&()*+,./:;<=>?@[\]^_`{|}~«»…“”‘')
re_pos = "[a-zA-Z-]+'[sS]$"
re_2apos = "^'.+'$"
re_numbers = '.*[0-9]+'
re_not = ".*[nN]'[tT]$"
re_future = ".*'[lL][lL]"
re_perfect = ".*'[vV][eE]"
re_gerund = ".*[iI][nN]'$"
re_quote = "^[A-Z-][a-z-]+"
re_2apos_quote = "''"

output_filename = 'autosorted_tokens.json'
filename = 'path_counter_dict.json'
all_tokens_counter = Counter()
with open(filename, 'r', encoding='utf-8') as f:
    path_counter_dict = json.load(f)
for path in path_counter_dict.keys():
    work_counter = path_counter_dict[path]
##    count all the tokens together 
    all_tokens_counter.update(work_counter)

def sort_out(r_exp, dic):
    '''Leaves in dict only tokens that do not match a regular expression'''
    return {token:dic[token] for token
            in dic.keys() if not re.match(r_exp, token)}

##leaves only tokens that do not contain punctuation from the string above
no_punct_counter = {token:all_tokens_counter[token]
                    for token in all_tokens_counter.keys()
                    if not set(token)&punct_set}

##sorts out all tokens ending with 's
no_single_possessives = sort_out(re_pos, no_punct_counter)
##sorts out all tokens ending that are inside two apostrophes
no_word_boundary_apos = sort_out(re_2apos, no_single_possessives)
##sorts out all tokens containing numbers
no_numbers = sort_out(re_numbers, no_word_boundary_apos)
##sorts out all tokens ending with n't
no_not = sort_out(re_not, no_numbers)
##sorts out all tokens ending with 'll
no_future = sort_out(re_future, no_not)
##sorts out all tokens ending with 've
no_perfect = sort_out(re_perfect, no_future)
##sorts out all tokens ending with in'
no_gerund = sort_out(re_gerund, no_perfect)
##sorts out all tokens beginning with apostrophe anda capital letter
no_quotes = sort_out(re_quote, no_gerund)
##sorts out all tokens containing 2 apostrophes one after another
no_2apos_quotes = sort_out(re_2apos_quote, no_quotes)

##print(len(all_tokens_counter))
##print(len(no_punct_counter))
##print(len(no_single_possessives))
##print(len(no_word_boundary_apos))
##print(len(no_numbers))
##print(len(no_not))
##print(len(no_future))
##print(len(no_perfect))
##print(len(no_gerund))
##print(len(no_quotes))
##print(len(no_2apos_quotes))
        
with open(output_filename, 'w', encoding='utf-8') as f:
    json.dump(no_2apos_quotes, f)

print(len(no_2apos_quotes))

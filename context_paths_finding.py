import json
import pandas as pd
from collections import Counter

f2read = 'to_add_context.csv'
json2load = 'path_counter_dict.json'
json2dump = 'token_paths_dict.json'

df = pd.read_csv(f2read)
tokens = []
for forms in set(df['forms'].values):
    if len(forms.split()) == 1:
        tokens.append(forms)
    else:
        for form in forms.split():
            tokens.append(form)

tokens = set(tokens)

token_path_dic = {token:[] for token in tokens}

with open(json2load, 'r', encoding='utf-8') as f:
    path_counter_dict = json.load(f)

for path, counter_dict in path_counter_dict.items():
    for word in counter_dict.keys():
        if word in token_path_dic.keys():
            token_path_dic[word].append(path)

with open(json2dump, 'w', encoding='utf-8') as f:
    json.dump(token_path_dic, f)

  

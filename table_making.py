import json
import pandas as pd
from collections import Counter


f2read = 'autosorted_tokens.json'
f2create = 'tokens_df.csv'

with open(f2read, 'r', encoding='utf-8') as f:
    tokens = json.load(f)
for token in tokens:
    if not "'" in token:
        print (token)
        
tokens_dict = {token.lower():[] for token in tokens}
for token in tokens:
    tokens_dict[token.lower()].append(token)
for k in tokens_dict.keys():
    tokens_dict[k] = " ". join(tokens_dict[k])

df = pd.DataFrame({"lowercase": [k for k in tokens_dict.keys()],
                  "forms": [v for v in tokens_dict.values()]})

df.to_csv(f2create, encoding='utf-8', index=False)
  

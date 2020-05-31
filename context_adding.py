import json
import pandas as pd
##from collections import Counter

f2read = 'to_add_context.csv'
json2load = 'token_contexts_dict.json'
f2create = '3contexts_df.csv'

df = pd.read_csv(f2read)
with open(json2load, 'r', encoding='utf-8') as f:
    token_contexts_dict = json.load(f)

for token, contexts in token_contexts_dict.items():
    if type(contexts) == list:
        token_contexts_dict[token] = "\n".join(token_contexts_dict[token])

lowercase_dict = {token.lower():[] for token in token_contexts_dict.keys()}
for token, contexts in token_contexts_dict.items():
    lowercase_dict[token.lower()].append(contexts)
lowercase_dict = {token:"\n".join(lowercase_dict[token]) for token in lowercase_dict.keys()}

df['contexts'] = df['lowercase'].apply(lambda x: lowercase_dict[x])

df.to_csv(f2create, encoding='utf-8', index=False)

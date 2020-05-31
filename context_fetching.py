import json
punkt='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~«»—–…“”‘'

json2load = 'token_paths_dict.json'
json2dump = 'token_contexts_dict.json'

with open(json2load, 'r', encoding='utf-8') as f:
    token_paths_dict = json.load(f)

token_contexts_dict = {token:[] for token in token_paths_dict.keys()}

for token, paths in token_paths_dict.items():
    contexts = []
    for path in paths:
        with open(path, 'r', encoding='utf-8') as f:
            line_list = f.read().split()
            for i, word in enumerate(line_list):
                if len(contexts) < 3: ## 3 contexts max
                    if (word.strip(punkt)==token) or (word==token):
                        try:
                            context = " ".join(line_list[i-5:i+5])
                            if len(context) > 1:
                                contexts.append(context)
                        except:                        
                            pass
    if contexts:
        contexts = "\n".join(contexts)
        token_contexts_dict[token] = contexts
        
with open(json2dump, 'w', encoding='utf-8') as f:
    json.dump(token_contexts_dict, f)

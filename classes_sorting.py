import pandas as pd

f2read = 'annotations.csv'
f2create = 'to_add_context.csv'

df = pd.read_csv(f2read)
df = df[df['if_interesting'] == 1]

def define_class(x):
    classes = []
    if x.endswith("'d"):
        classes.append('would')
    if 'ss' in x:
        classes.append('hiss')
    if 'zz' in x:
        classes.append('buzz')
    if classes:
        return ' '.join(classes)
    else:
        return None

df['n_of_variants'] = df['forms'].apply(lambda x: len(x.split()))
df['class'] = df['lowercase'].apply(lambda x: define_class(x))

df.to_csv(f2create, encoding='utf-8', index=False)
  

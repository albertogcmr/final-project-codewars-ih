# D3

# https://www.machinelearningplus.com/plots/top-50-matplotlib-visualizations-the-master-plots-python/#33.-Treemap

import matplotlib.pyplot as plt
import pandas as pd
import json
from acquisition.languages import get_languages

# {"name": "php", "size": 2},
def create_d3(data): 
    df = data
    idiomas = []
    languages = [lang for lang in get_languages() if lang in df.columns]
    for col in languages: 
        idiomas.append({'name': col, "size": int(df[col].sum())})
    res = {"name": "Lenguajes","children": [{"name": "Lenguajes","children": [{"name": "Lenguajes","children": idiomas}]}]}
    
    return json.dumps(res, ensure_ascii=False)

def save_d3_languages_json(lang_json, filename='../representacion_d3/lenguajes.json'): 
    with open(filename, 'w') as f: 
        f.write(lang_json)

# print(get_languages())


CLEAN_CSV_PATH = "output/codewar_users_clean.csv"
JSON_LANGS_OUTPUT = 'representacion_d3/lenguajes.json'


def clean_lang(lang): 
    # misma limpieza que los nombres de las columnas
    res = lang.replace(' ', '_').replace('.', '').lower()
    return res

df_raw = pd.read_csv(CLEAN_CSV_PATH)

languages = [clean_lang(lang) for lang in get_languages()]
languages = [lang for lang in languages if lang in df_raw.columns]

# pip install squarify
import squarify 

# Import Data

# Prepare Data
labels = languages
print(labels)
sizes = df_raw[[col for col in languages]].sum(axis=1)
colors = [plt.cm.Spectral(i/(1+float(len(labels)))) for i in range(len(labels))]

# Draw Plot
plt.figure(figsize=(12,8), dpi= 80)
# squarify.plot(sizes=sizes, label=labels, color=colors, alpha=.8)
squarify.plot(sizes=[1,2,3], label=['java', 'c', 'python'], color=['red','green','blue'], alpha=.8)

# Decorate
plt.title('Treemap of Codewars ranks')
plt.axis('off')
plt.show()
import re
import pandas as pd

"""
Extract the url address in the text description 
Replace all url addresses with <url> tags in the original text string

"""

df = pd.read_csv("./url_data.csv")

url_ptn = r'\bhttps?://\S+\b'

for idx,row in df.iterrows():
    match = re.findall(url_ptn,row['text'])
    res = re.sub(url_ptn,'<url>',row['text'])
    df.loc[idx,'processed text'] = res
    if len(match)>0:
        df.loc[idx,'website'] = " ".join(match)
    
df.to_csv('./processed_url_data.csv',index=False)
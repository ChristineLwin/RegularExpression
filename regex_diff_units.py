import pandas as pd
import re

"""
Use Regular Expression to extract: 
1. substring between start string and end string using lookahead and lookbehind
2. values with different units
"""
df = pd.read_csv('raw_data.csv')

# pattern using lookbehind and lookahead 
ptn = r'.*(?<=allergic to) (\D*?)(?=medication)'

# filter number of year and month
ptn_y = r'(\d+(?:\.\d+)?)\s(?=[years|year|yrs])'
ptn_m = r'(\d{1,3}?)\s(?=[months|mns])'

for idx,row in df.iterrows():
    match = re.compile(ptn).search(row['description'])
    if match :
        df.loc[idx,'Allgery'] = match.group(1).replace("\\n","")

    # for line in des:
    match1 = re.match(ptn_y,row['text'])
    match2 = re.search(ptn_m,row['text'])
    if match1:
        df.loc[idx,'year'] = match1.group(1)
    if match2:
        df.loc[idx,'month'] = match2.group(1)

#write the parsed dataframe to a file
df.to_excel("processed_raw_data.xlsx",index=False)
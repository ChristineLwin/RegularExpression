import re
import pandas as pd

"""
Use Regular Expression to extract the following information:
1. Zip Code from the address information
2. BMI values from the unstructured description text string
3. phone numbers and email addresses from the text string 
"""

# read test file 
df = pd.read_csv("test_data.csv")

# assume every zip code has 5 digit 
zipcode_pt = r'\d{5}'

# string must precede with "bmi" to capture bmi value
bmi_pt = r'(?<=bmi)(\D*)(\d{0,2}\.?\d?)'

# 10 digit phone number
ph_pt = r'\(?\d{3}\)?\D?\d{3}\D?\d{4}'

# extract email info - assume the domain name is up to 2-4 characters only
# extract all email addresses
email_pt = r'([a-zA-Z0-9_.-]+@[a-zA-Z0-9_.-]+\.[a-zA-Z.]{2,4})'

for idx,row in df.iterrows():
    match_zip = re.search(zipcode_pt,row['Address']) 
    if match_zip:
        df.loc[idx,'Zipcode'] = match_zip.group()

    match_bmi = re.search(bmi_pt, row['Description'])
    if match_bmi:
        df.loc[idx,'BMI'] = match_bmi.group(2)
    
    match_ph = re.search(ph_pt, row['Contact Details'])
    if match_ph:
        df.loc[idx,'Phone'] = match_ph.group()

    match_email = re.findall(email_pt, row['Contact Details'])
    if len(match_email)>0:
        for m in match_email:
            df.loc[idx,'Email'] = ";".join(match_email)
    

#write the parsed dataframe to a file
df.to_excel("processed_test_data.xlsx",index=False)
import requests, os, urllib, sys, csv, secrets, string
import pandas as pd

#method to generate passwords
def genpw():
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(8))
    return(password)

#get the csv
g = requests.get('https://api.github.com/gists/[protected]')
jadd = g.json()
for key in jadd['files']:
    print(key)
    jf = urllib.request.urlretrieve(jadd['files']['users.csv']['raw_url'],key)

#append the desired data and output
password = pd.Series([])
UPN = pd.Series([])
csvfile = pd.read_csv('users.csv')

for i in range(len(csvfile)):
    password[i] = genpw()
    fname = csvfile.at[i,'Firstname']
    lname = csvfile.at[i,'Lastname']
    UPN[i] = fname.lower()+'.'+lname.lower()+'@domain.com'
csvfile.insert(3, "password", password)
csvfile.insert(4,"UPN", UPN)
newcsvfile = csvfile.sort_values('Firstname')
newcsvfile.to_csv('users.csv', index=False)

import pandas as pd
import subprocess

df = pd.read_csv('links.txt',header=None ,skiprows=0)

with open('results.txt', 'a') as out:
    for link in df[0]:
        result = subprocess.check_output("curl '{0}'".format(link), shell=True )
        out.write(str(result) + '\n\n\n')

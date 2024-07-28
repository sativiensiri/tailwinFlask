import os
import json

path = os.getcwd()
data = os.path.join(path , "data.json")

with open(data,"r",encoding='utf-8') as f:
  jobs = json.load(f)

# for job in jobs:
#     print(job['id'], job['type'], job['company'])

id = "afbd99e0-561a-4add-a147-6f96d820b244"

for job in jobs:
    if job['id'] == id:
        jb = job
        break

print(jb)
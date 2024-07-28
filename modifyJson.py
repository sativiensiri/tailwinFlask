import os
import json

path = os.getcwd()
data = os.path.join(path , "data.json")

with open(data,"r",encoding='utf-8') as f:
  jobs = json.load(f)

id = "e3268c79-614c-4978-8f22-e6495c1e067f"
newDescription = "In this article, we define company descriptions, review their key elements, provide tips for writing and list examples you can reference when crafting your own."

for job in jobs:
    if job['id'] == id:
        jb = job
        jb['description'] = newDescription
        break

modified_json = json.dumps(jobs)

print('After Modifying:', modified_json)


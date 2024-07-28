import json

with open("mydata.json", "r") as jsonfile:
    data = json.load(jsonfile)

new_data = ...  # Download new data from your API.
data.update(new_data)
# Alternatively, if the outmost data structure in the JSON file is a list:
# data.append(new_data)

with open("mydata.json", "w") as jsonfile:
    json.dump(data, jsonfile)
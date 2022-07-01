## Exercise 1: Convert the following dictionary into JSON format
import json
data = {"key1" : "value1", "key2" : "value2"}
Jsondata=json.dumps(data)
print(Jsondata)

## Exercise 2: Access the value of key2 from the following JSON
sampleJson ={"key1": "value1", "key2": "value2"}
res=sampleJson["key2"]
print("Access value of key2=",res)

## or convert json to dict
sampleJson = """{"key1": "value1", "key2": "value2"}"""
data = json.loads(sampleJson)
print("Value of key2=",data['key2'])

## Exrcise 3.PrettyPrint following JSON data with indent level 2 and key-value separators should be (",", " = ").
sampleJson = {"key1": "value1", "key2": "value2","key3":"value3"}
prettyPrintedJson=json.dumps(sampleJson,indent=2,separators=(","," = "))
print(prettyPrintedJson)

## Exercise 4: Sort JSON keys in and write them into a file Sort following JSON data alphabetical order of keys
sampleJson = {"id" : 1, "name" : "value2", "age" : 29}

print("Started writing JSON data into a file")
with open ("sampleJson.json",'w') as fp:
    json.dump(sampleJson,fp,indent=4,sort_keys=True)
print("Done writing JSON data into a file")

##  Exercise 5: Access the nested key ‘salary’ from the following JSON
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

data=json.loads(sampleJson)
print("key of salary is =",data["company"]["employee"]["payble"]["salary"])

## Exercise 6: Convert the following Vehicle Object into JSON
import json
from json import JSONEncoder
class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

class VehicleEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)
Json1=json.dumps(vehicle,indent=4,cls=VehicleEncoder)
print(Json1)

## Exercise 7: Convert the following JSON into Vehicle Object

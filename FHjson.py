import json

record1= {"name":"Java","price":1000,'Flag':True,'Author':None}


#loads() , dumps(), load(), dump()

'''d1=json.loads(record)
print(d1)
print(d1['price'])
print(type(record))
print(type(d1))

data=json.dumps(d1)
print(data)'''

#read and write operation on JSON files

with open("file2.json","w") as fp:
    json.dump(record1,fp)



with open("file2.json","r") as fp:
    result=json.load(fp)
    print(result)




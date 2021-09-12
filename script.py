import os
import json

dev_token = "PYl6A9mX8LtpxtNOzgRcIOjztSBYrgoa9QRzATMC"
#name = "test group"

names = ["CSCE 221", "CSCE 222", "CSCE 223"]

#str = 'curl -X POST -H "Content--Type: application/json" -d "{"name": "' + name + '"}" https://api.groupme.com/v3/groups?token=' + dev_token
#os.system(str)

#str = "curl -X POST -H \"Content-Type: application/json\" -d '{\"name\": \"Family\"}' https://api.groupme.com/v3/groups?token=PYl6A9mX8LtpxtNOzgRcIOjztSBYrgoa9QRzATMC"
#os.system(str)

f = open("dummy.json")

all_courses = json.load(f)

for i in all_courses["classes"]:
    dep = i["department"]
    course = i["course"]

    course_name = dep + " " + course

    test = "department = " + dep + ", course = " + course
    print(course_name)

    #str = "curl -X POST -H \"Content-Type: application/json\" -d '{\"name\": \"" + name + "\"}' https://api.groupme.com/v3/groups?token=" + dev_token
    #os.system(str)

#curl -X POST -H "Content-Type: application/json" https://api.groupme.com/v3/groups/70873511/destroy?token=PYl6A9mX8LtpxtNOzgRcIOjztSBYrgoa9QRzATMC
data = curl -X GET -H "Content-Type: application/json" https://api.groupme.com/v3/groups?token=PYl6A9mX8LtpxtNOzgRcIOjztSBYrgoa9QRzATMC

for i in data
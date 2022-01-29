import os
import json

dev_token = "PYl6A9mX8LtpxtNOzgRcIOjztSBYrgoa9QRzATMC"

def load_groupmes():

    f = open("demo.json")

    all_courses = json.load(f)

    for i in all_courses["classes"]:
        dep = i["department"]
        course = i["course"]
        prof = i["instructor"]

        course_name = dep + " " + course + " " + prof

        test = "department = " + dep + ", course = " + course
        #print(course_name)

        str = "curl -X POST -H \"Content-Type: application/json\" -d '{\"name\": \"" + course_name + "\"}' https://api.groupme.com/v3/groups?token=" + dev_token
        os.system(str)


def delete_groupmes():
    del_ids = [70879951, 70880083]
    for ids in del_ids:

        deletee = 'curl -X POST -H "Content-Type: application/json" https://api.groupme.com/v3/groups/' + str(ids) + '/destroy?token=' + dev_token
        os.system(deletee)

if __name__ == "__main__":
    inp = input("load or delete groupmes: ")
    if inp == "load":
        load_groupmes()
    else:
        delete_groupmes()
    
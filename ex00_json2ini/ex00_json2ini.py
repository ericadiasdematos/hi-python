import json,os

file = "jsonFile.json"
string = ""

if(os.path.exists(file)):
    with open(file, "r") as file:

        #file = json.loads(file.read())
        #print(file)

        data = json.load(file)

        for section in data.keys():
            string += "[" + section + " ]" + "\n"
            sectionElement = data[section]
            for key in sectionElement.keys():
                string += str(key) + " = " + str(sectionElement[key]) + "\n"
            string += "\n"
        with open('file.ini', 'w') as file:
            file.write(string)
            print("Job done!")

else:
    print("file does not exist")
import requests

server = "http://vcm-7631.vm.duke.edu:5002"
r = requests.get(server + "/get_patients/jbw70")
print(r.text)


d = requests.get(server + "/get_blood_type/F8")
print(d.text)

d = requests.get(server + "/get_blood_type/F5")
print(d.text)

out_data = {"Name": "jbw70", "Match":  "No"}
r = requests.post(server + "/match_check",
                  json=out_data)
print(r.text)

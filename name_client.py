import requests

out_data = {
    "name": "Jenna White",
    "net_id": "jbw70",
    "e-mail": "jenna.white@duke.edu"
}
r = requests.post("http://vcm-21170.vm.duke.edu:5000/student",
                  json=out_data)

print(r.status_code)
print(r.text)

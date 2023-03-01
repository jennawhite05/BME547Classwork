import requests

out_data = {"user": "jbw70", "message": "Hello"}
r = requests.post("http://vcm-21170.vm.duke.edu:5001/add_message",
                  json=out_data)

print(r.status_code)
print(r.text)

g = requests.get("http://vcm-21170.vm.duke.edu:5001/get_messages/nh170")
print(g.text)

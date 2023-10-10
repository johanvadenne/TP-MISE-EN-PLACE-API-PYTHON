import requests
import pprint


while 1:
    try:
        entree = input("num employer:\n")
        if entree == "STOP":
            break
        api_url = "http://127.0.0.1:5000/employees/"+str(entree)
        response = requests.get(api_url)
        pprint.pprint(response.json())
    except:
        continue
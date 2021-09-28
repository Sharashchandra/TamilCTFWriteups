import requests
import bs4
import json

inputs = "abcdefghijklmnopqrstuvwxyz0123456789"

cringe_mappings = {}

def get_values():
    for char in inputs:
        data = {"text": char}
        response = requests.post("http://45.79.195.170:5000/encode", data=data)
        soup = bs4.BeautifulSoup(response.content, "html.parser")
        result = soup.select(".result")[0].text
        value = result.split(":")[-1].replace("\n", "").strip()
        cringe_mappings[value] = char

    with open("cringe_mappings.json", "w+") as f:
        f.write(json.dumps(cringe_mappings))

def decode():
    final_string = ""
    values = ["cR1Ng3e", "crinG3", "cringE", "cringe", "cRINGe", "cRINGe", "cring3", "crinG3", "cringE", "cringE", "cRinG3", "Cr1nGe", "cRimG3", "criNG3", "cRinge", "cRimG3", "cringe", "cR1Ng3e", "cRiNge", "cRinG3", "cR1Ng3", "CrInGe", "cRInGE", "cr1ngE", "criNG3", "cringE", "cring3", "cRinge", "cR1Ng3", "crinGE", "cringE", "criNgee", "cRinG3", "CrInGe"]
    mapping = dict()
    with open("cringe_mappings.json", "r") as f:
        mapping = json.loads(f.read())
    
    for value in values:
        print(mapping[value])
        final_string += mapping[value]
    print(final_string)

get_values()
decode()

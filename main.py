
import requests


class RecupereAPI:
  def __init__(self, url, headers):
    self.url = url
    self.headers = headers
  

  def Informations(self):
    inf = requests.get(self.url, self.headers)
    return inf
  
Chapter_id = input("Chapter?")
url = f"https://api.quran.com/api/v4/chapters/{Chapter_id}"
headers = {"Content-Type": "application/json"}


Information = RecupereAPI(url, headers)



response = Information.Informations()
print(response.json()) 

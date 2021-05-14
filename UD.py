#Urban Dictionary search by Exabyte
#Version 1.0.0

from bs4 import BeautifulSoup
import requests

def search(query):
    query = "https://www.urbandictionary.com/define.php?term=" + query
    query = query.replace(' ', "%20")
    query = requests.get(query)
    
    if query.status_code == 200:
        
        soup = BeautifulSoup(query.text, "lxml")
        Result = {
            "Name" : soup.find("div", class_="def-header").text,
            "Meaning" : soup.find("div", class_="meaning").text,
            "Example" : soup.find("div", class_="example").text,
            "Contributor" : soup.find("div", class_="contributor").text,
        }
        
        return Result

    else:
        return None

version = "V1.0.1"
        


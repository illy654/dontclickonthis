from bs4 import BeautifulSoup
import requests
import pandas as pd

data = requests.get("https://www.worlddata.info/average-penissize.php")

soup = BeautifulSoup(data.text, "html.parser")

penisdata = soup.find_all("tr")
penisdata.pop(0)

country = []
size = []

for x in range(len(penisdata)):
    country.append(penisdata[x].find("td").text)
    length = penisdata[x].findAll("td")[1].text
    size.append(float(length[0:-3]))

df = pd.DataFrame(size,index=country,columns=["Size"])
df["Size"] = df["Size"] * 0.393701
df["Main sex that has dicks"] = "Male"
df.columns =[ "Average Dick Size", "Main sex that has dicks"]
df.to_excel("output.xlsx")
import requests

sname="Farzana"
fname= "Tamim"

url = "https://love-calculator.p.rapidapi.com/getPercentage"

querystring = {"sname":sname,"fname":fname}

headers = {
	"content-type": "application/octet-stream",
	"X-RapidAPI-Key": "9a81a971b3msh34cb1c391aed569p10a071jsnf95a632ba13e",
	"X-RapidAPI-Host": "love-calculator.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
x=response.json()
print(x['result'])
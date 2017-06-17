
import requests
from bs4 import BeautifulSoup

page = requests.get("http://forecast.weather.gov/MapClick.php?lat=40.742551138125634&lon=-73.92077486866447#.WUSVfxPyuV6")
soup = BeautifulSoup(page.content, 'html.parser')
weather = soup.find_all("p", "myforecast-current")

print(weather[0].getText())

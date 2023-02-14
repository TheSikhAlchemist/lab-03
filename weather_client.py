import requests
from typing import Dict

# connect to a "real" API

## Example: OpenWeatherMap
URL = "https://api.openweathermap.org/data/2.5/weather"

# TODO: get an API key from openweathermap.org and fill it in here!
API_KEY = "787142aaef3731cfdd2e9ad31cda897c"

def get_weather(city) -> Dict:
    res = requests.get(URL, params={"q": city, "appid": API_KEY})
    return res.json()

# TODO: try connecting to a another API! e.g. reddit (https://www.reddit.com/dev/api/)

def get_news() -> None:
    base_url = "https://newsapi.org/v2/everything?"

    params = {
        "q": "python", 
        "pageSize": 20, 
        "apiKey": "21e1d2528b9d44d79953725b95dbd946"
    }
    res1 = requests.get(base_url, params=params)
    if res1.status_code == 200:
        articles = res1.json()["articles"]
        for article in articles:
            print(article["title"])
            print(article["description"])
            print()
    else:
        # Print the error message
        print("Error:", res1.json()["message"])

def main():
    temp = get_weather("London")
    print(temp)
    print()
    get_news()

if __name__ == "__main__":
    main()

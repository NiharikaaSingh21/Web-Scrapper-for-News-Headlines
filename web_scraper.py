import requests
from bs4 import BeautifulSoup

def scrape_headlines():
    url = "https://www.hindustantimes.com/latest-news"  

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
    }

    try:
        response = requests.get(url, headers=headers)

        
        if response.status_code != 200:
            print("Failed to fetch page. Status code:", response.status_code)
            return

        # Parse HTML
        soup = BeautifulSoup(response.text, "html.parser")

        headlines = soup.find_all("h2")

        if not headlines:
            print("No headlines found!")
            return

        # Save to file
        with open("news.txt", "w", encoding="utf-8") as file:
            for h in headlines:
                text = h.get_text(strip=True)
                if text:
                    file.write(text + "\n")

        print("Headlines scraped successfully! Check 'news.txt'.")

    except Exception as ex:
        print("An error occurred:", ex)

scrape_headlines()

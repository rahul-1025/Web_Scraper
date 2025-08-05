import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"

print("📡 Fetching website content...")

response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

headlines = soup.find_all('h2')

print("🔍 Total headlines found:", len(headlines))

headline_list = []
for tag in headlines:
    text = tag.get_text(strip=True)
    if text:
        headline_list.append(text)

with open("news_headlines.txt", "w", encoding="utf-8") as file:
    for title in headline_list:
        file.write(title + "\n")

print("✅ Headlines saved to 'news_headlines.txt'")
print("📝 Sample Headlines:")
for i, headline in enumerate(headline_list[:5]):
    print(f"{i+1}. {headline}")

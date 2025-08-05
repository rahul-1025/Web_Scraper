 📌 Objective
Scrape top news headlines from a news website using Python and save them in a `.txt` file.

---

 🧰 Tools Used
- Python 3
- [requests](https://pypi.org/project/requests/) – to fetch website HTML
- [BeautifulSoup (bs4)](https://pypi.org/project/beautifulsoup4/) – to parse and extract headlines

---

 📝 Task Description
- Use `requests` to download HTML content of a news website
- Use `BeautifulSoup` to extract headlines (`<h2>` tags)
- Save all scraped headlines into a text file named `news_headlines.txt`

---

 📂 Files Included
- `scraper.py` – Python script that performs the scraping
- `news_headlines.txt` – Output file containing scraped headlines
- `README.md` – This documentation file

---

 ▶️ How to Run

1. Install required libraries (if not already installed):

   
   pip install requests beautifulsoup4


2. Run the Python script:

   
   python scraper.py
   

3. Output:

   - The terminal will show how many headlines were found.
   - All headlines will be saved to `news_headlines.txt`.

---

 🌐 Source Website
- [BBC Latest News](https://www.bbc.com/news) – used for scraping headlines.


 ✅ Sample Output (Terminal)


📡 Fetching website content...
🔍 Total headlines found: 20
✅ Headlines saved to 'news_headlines.txt'
📝 Sample Headlines:
1. Headline 1
2. Headline 2
3. Headline 3
4. Headline 4
5. Headline 5


import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime as dt

def news_collector(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    news = []

    articles = soup.find_all('article')
    for article in articles[:10]:
        title = article.find('h3').text.strip()
        link = "https://www.tecmundo.com.br" + article.find('a')['href']

        news.append({
            'title': title,
            'link': link,
        })

    return news

def save_collection(news):
    current_dt = dt.now().strftime('%Y%m%d')
    df = pd.DataFrame(news)
    df.to_csv(f'output/news_tec_{current_dt}.csv', index=False, encoding='utf-8')
    print(f"[✓] {len(news)} successfully saved news.")

if __name__ == '__main__':
    save_collection(news_collector("https://www.tecmundo.com.br/novidades"))
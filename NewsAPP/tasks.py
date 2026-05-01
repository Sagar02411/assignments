import os
import requests
from datetime import datetime, timedelta
from celery import Celery
from database import SessionLocal
from models import News
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

celery_app = Celery(
    'tasks',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0')

celery_app.conf.beat_schedule = {
    'fetch-news-every-minute': {
        'task': 'tasks.fetch_and_store_news',
        'schedule': timedelta(minutes=1),
    },
}
celery_app.conf.timezone = 'UTC'

@celery_app.task
def fetch_and_store_news():
    api_key = os.getenv("API_KEY")
    url = (
        'https://newsapi.org/v2/top-headlines?'
        'sources=bbc-news&'
        f'apiKey={api_key}'
    )
    response = requests.get(url)
    news_data = response.json()
    print(news_data)

    db = SessionLocal()
    try:
        db_news = News(
            source_id=article.get("source", {}).get("id"),
            source_name=article.get("source", {}).get("name"),
            author=article.get("author"),
            title=article.get("title"),
            description=article.get("description"),
            url=article_url,
            url_to_image=article.get("urlToImage"),
            published_at=published_at,
            content=article.get("content"),
            created_at=datetime.utcnow(),
            )
        db.add(db_news)

        db.commit()
        print("News articles saved successfully.")
    except Exception as e:
        db.rollback()
        print(f"Error saving news: {e}")
        raise
    finally:
        db.close()
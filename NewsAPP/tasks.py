import os
import requests
from datetime import datetime, timedelta
from celery import Celery
from database import SessionLocal
from models import News
import redis
# from rq import queue

# r = redis.Redis()
# q = Queue(connection = r)

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
    api_key = 'API_KEY'
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
        for article in news_data.get("articles", []):
            db_news = News(
                source_id=article.get("source", {}).get("id"),
                source_name=article.get("source", {}).get("name"),
                author=article.get("author"),
                title=article.get("title"),
                description=article.get("description"),
                url=article.get("url"),
                url_to_image=article.get("urlToImage"),
                published_at=article.get("publishedAt"),
                content=article.get("content"),
                created_at=datetime.now(),
            )
            db.add(db_news)
        db.commit()
        
    finally:
        db.close()
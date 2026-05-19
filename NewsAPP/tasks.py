from celery import Celery
import requests
from datetime import datetime,timedelta
import os
from dotenv import load_dotenv
import flask_app

load_dotenv()

celery_app = Celery('tasks', broker='redis://127.0.0.1:6379', backend='redis://127.0.0.1:6379')

celery_app.conf.beat_schedule = {
    'fetch-news-every-minute': {
        'task': 'tasks.fetch_and_store_news',
        'schedule': timedelta(minutes=1),
    },
}
celery_app.conf.timezone = 'UTC'

@celery_app.task
def fetch_and_store_news():
    try:
        from flask_app.utils import create_app
        from flask_app.extensions import db
        from flask_app.models import News

        app = create_app()
        print(f'after:{app}')
        with app.app_context():                  
            api_key = os.getenv("API_KEY")
            url = 'https://newsapi.org/v2/top-headlines?' \
                'sources=bbc-news&' \
                    f'apiKey={api_key}'
                    
            response = requests.get(url)
            news_data = response.json()
            #db = db_session()
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
                    created_at = datetime.now()
                    )
                print(f"db_news {db_news}")
                db.session.add(db_news)
                print("done")
                db.session.commit()
                db.session.close()
    except Exception as e:
        print(f"error {e}")

    #     db.session.commit()
    #     db.session.close()
        raise e

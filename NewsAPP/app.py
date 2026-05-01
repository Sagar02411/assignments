from flask import Flask, jsonify
from dotenv import load_dotenv
from database import engine, Base
from models import News  
from tasks import celery_app, fetch_and_store_news

load_dotenv()
Base.metadata.create_all(bind=engine)

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return jsonify({"status": "running",
                    "message": "News API is running"})

@app.route('/fetch', methods=['GET'])
def fetch_now():
    fetch_and_store_news.delay()
    return jsonify({"status": "queued",
                    "message": "smthh"})

if __name__ == '__main__':
    app.run(debug=True)
    
    
# celery -A tasks.celery_app worker --loglevel=info
# celery -A tasks.celery_app beat --loglevel=info
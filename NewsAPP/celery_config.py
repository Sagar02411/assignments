# from celery.schedules import crontab
# from datetime import timezone
# import redis
# r = redis.Redis(host='localhost', port=6379, decode_responses=True)

# broker_url = "redis://localhost:6379/0"
# result_backend = "redis://localhost:6379/0"

# task_serializer = "json"
# result_serializer = "json"
# accept_content = ["json"]

# timezone = "UTC"
# enable_utc = True

# beat_schedule = {
#     "fetch-bbc-news-every-minute": {
#         "task": "tasks.fetch_and_store_news",   
#         "schedule": 60.0,                        
#     },
# }
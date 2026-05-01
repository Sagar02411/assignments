
from flask_app.utils import create_app
app = create_app()


if __name__ == '__main__':
    app.run(debug=True)

# # celery -A tasks.celery_app worker --loglevel=info
# # celery -A tasks.celery_app beat --loglevel=info
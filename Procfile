web: gunicorn src.config.asgi:application -k uvicorn.workers.UvicornWorker
worker: celery --app=src.config.celery worker

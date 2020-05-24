import redis
from app.config import Config
from rq import Worker, Queue, Connection

listen = ['high', 'low', 'default']
conn = redis.from_url(Config.REDIS_URL)

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()

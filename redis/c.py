import time
import redis
redis_pool = redis.ConnectionPool(host='121.37.95.198',port=6379,password='foobared#$AZd',db=0)
redis_conn = redis.Redis(connection_pool=redis_pool)
def producer():
    for i in range(10):
        redis_conn.lpush('int_queue', i)
        time.sleep(1)

if __name__ == '__main__':
    producer()



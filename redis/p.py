






# -----------消息端---------------------------
import time
import redis
redis_pool = redis.ConnectionPool(host='121.37.95.198',port=6379,password='foobared#$AZd',db=0)
redis_conn = redis.Redis(connection_pool=redis_pool)

def consumer():
    while True:
        data = redis_conn.rpop('int_queue')
        if data is None:
            time.sleep(5)
            continue
        else:
            time.sleep(5)
            print(data)   # 消费数据

if __name__ == '__main__':
    consumer()
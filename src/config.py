import os

def config():
    return {
        'host': os.environ.get('DB_HOST'),
        'database': os.environ.get('DB_NAME'),
        'port': os.environ.get('DB_PORT'),
        'user': os.environ.get('DB_USER'),
        'password': os.environ.get('DB_PASSWORD'),
        'connect_timeout': os.environ.get('DB_CONNECT_TIMEOUT', 5)
    }

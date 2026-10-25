from datetime import datetime, timedelta

REFRESH_TOKEN_EXPIRE_TIME = datetime.now() + timedelta(days=1)
ACCESS_TOKEN_EXPIRE_TIME = datetime.now() + timedelta(minutes=10)
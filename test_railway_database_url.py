import os

from sqlalchemy.engine import make_url

DATABASE_URL = os.getenv("DATABASE_URL")

print("DATABASE_URL exists:", DATABASE_URL is not None)

if DATABASE_URL:
    url = make_url(DATABASE_URL)

    print("Driver:", url.drivername)
    print("Host:", url.host)
    print("Port:", url.port)
    print("Database:", url.database)

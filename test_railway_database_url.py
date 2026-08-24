import os

from sqlalchemy.engine import make_url

database_url = os.getenv("DATABASE_URL")

print("DATABASE_URL exists:", database_url is not None)

if database_url:
    print("URL length:", len(database_url))
    print("Contains '/':", "/" in database_url)
    print("Contains '=':", "=" in database_url)

    try:
        url = make_url(database_url)

        print("SQLAlchemy parsing: SUCCESS")
        print("Driver:", url.drivername)
        print("Host:", url.host)
        print("Port:", url.port)
        print("Database:", url.database)
        print("Username exists:", url.username is not None)
        print("Password exists:", url.password is not None)

    except Exception as error:
        print("SQLAlchemy parsing: FAILED")
        print("Error:", error)

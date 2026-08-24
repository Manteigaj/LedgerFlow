import os

database_url = os.getenv("DATABASE_URL")

print("DATABASE_URL exists:", database_url is not None)

if database_url:
    print("DATABASE_URL length:", len(database_url))

    if "@" in database_url:
        _, host_part = database_url.rsplit("@", 1)
        print("Masked DATABASE_URL: ***@" + host_part)
    else:
        print("Masked DATABASE_URL: [no @ found]")

    print(
        "Starts with postgresql:",
        database_url.startswith("postgresql"),
    )

    print(
        "Contains railway.internal:",
        "railway.internal" in database_url,
    )

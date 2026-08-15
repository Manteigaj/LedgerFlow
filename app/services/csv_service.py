import csv


def read_csv(content: str):
    reader = csv.DictReader(content.splitlines())

    data = []

    for row in reader:
        data.append(
            {
                "date": row["date"],
                "description": row["title"],
                "amount": row["amount"],
            }
        )

    return data


def convert_amount(amount):
    amount = amount.strip()

    amount = amount.replace(" ", "")

    if "," in amount:
        amount = amount.replace(".", "")
        amount = amount.replace(",", ".")

    return float(amount)

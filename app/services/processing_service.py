from sqlalchemy.orm import Session

from app.crud.transaction import save_transactions
from app.services.categorization import categorize
from app.services.csv_service import read_csv


def process_transactions(
    db: Session,
    text: str,
):
    data = read_csv(text)

    for transaction in data:
        category = categorize(transaction["description"])

        transaction["category"] = category

    save_transactions(db, data)

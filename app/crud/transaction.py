from datetime import datetime
from sqlalchemy.orm import Session
from app.crud.category import get_or_create_category
from app.models import Transaction
from app.services.csv_service import convert_amount


def save_transactions(
    db: Session,
    rows,
    user_id: int,
):
    transactions = []

    for row in rows:
        category = get_or_create_category(
            db=db,
            name=row["category"],
        )

        transaction = Transaction(
            date=datetime.strptime(
                row["date"],
                "%Y-%m-%d",
            ).date(),
            description=row["description"],
            amount=convert_amount(row["amount"]),
            category_id=category.id,
            user_id=user_id,
        )

        transactions.append(transaction)

    db.add_all(transactions)
    db.commit()

    return len(transactions)

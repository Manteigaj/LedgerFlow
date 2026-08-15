from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models import Category


def create_category(db: Session, name: str) -> Category:
    category = Category(name=name)

    db.add(category)
    db.commit()
    db.refresh(category)

    return category


def get_category_by_id(
    db: Session,
    category_id: int,
) -> Category | None:
    return db.get(Category, category_id)


def get_category_by_name(
    db: Session,
    name: str,
) -> Category | None:
    stmt = select(Category).where(Category.name == name)

    return db.scalar(stmt)


def list_categories(db: Session) -> list[Category]:
    stmt = select(Category).order_by(Category.name)

    return list(db.scalars(stmt))


def get_or_create_category(
    db: Session,
    name: str,
) -> Category:
    category = get_category_by_name(db, name)

    if category is not None:
        return category

    return create_category(db, name)

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.auth.password import hash_password, verify_password
from app.auth.jwt import create_access_token
from app.crud.user import create_user, get_user_by_username
from app.database import get_db
from app.schemas import UserCreate, UserResponse, LoginRequest

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post(
    "/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED
)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    existing_user = get_user_by_username(db=db, username=user_data.username)

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Username already registered."
        )

    hashed_password = hash_password(user_data.password)

    user = create_user(
        db=db, username=user_data.username, hashed_password=hashed_password
    )

    return user


@router.post("/login")
def login(
    login_data: LoginRequest,
    db: Session = Depends(get_db),
):
    user = get_user_by_username(
        db=db,
        username=login_data.username,
    )

    if not user or not verify_password(
        login_data.password,
        user.password,
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password.",
        )

    access_token = create_access_token(data={"sub": str(user.id)})

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }

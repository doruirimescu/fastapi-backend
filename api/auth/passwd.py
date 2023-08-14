from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def is_pwd_valid(plain_text_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_text_password, hashed_password)


def generate_hashed_pwd(plain_text_password: str) -> str:
    return pwd_context.hash(plain_text_password)

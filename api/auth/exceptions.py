from fastapi import HTTPException, status


class LoginExpired(Exception):
    pass


class UserExists(Exception):
    pass


class UserUnauthorized(Exception):
    pass


LOGIN_EXPIRED = LoginExpired("Login expired")
USER_EXISTS = UserExists("Username already exists")
USER_UNAUTHORIZED = UserUnauthorized("Could not validate credentials")

HTTP_USER_UNAUTHORIZED = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)

HTTP_USER_EXISTS = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Username already exists",
)


HTTP_LOGIN_EXPIRED = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Login expired",
)

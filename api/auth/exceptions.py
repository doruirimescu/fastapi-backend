from fastapi import HTTPException, status

USER_UNAUTHORIZED = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)

USER_EXISTS = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Username already exists",
)

LOGIN_EXPIRED = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Login expired",
)

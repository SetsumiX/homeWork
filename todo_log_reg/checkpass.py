from fastapi.exceptions import HTTPException

def check_id(user_id):
    if user_id is None:
        raise HTTPException(status_code=401, detail="Не авторизирован")
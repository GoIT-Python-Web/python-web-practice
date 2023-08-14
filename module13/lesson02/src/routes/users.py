from fastapi import APIRouter, HTTPException, Depends, status, File, UploadFile
from fastapi.security import OAuth2PasswordRequestForm, HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session
import cloudinary
import cloudinary.uploader

from src.database.connect import get_db
from src.database.models import User
from src.schemas import UserModel, UserResponse, TokenModel, UserDb
from src.repository import users as repository_users
from src.services.auth import auth_service
from src.conf.config import settings

router = APIRouter(prefix='/users', tags=["users"])


@router.get("/me", response_model=UserDb)
async def read_users_me(current_user: User = Depends(auth_service.get_current_user)):
    return current_user


@router.patch("/avatar", response_model=UserDb)
async def update_cat(file: UploadFile = File(), db: Session = Depends(get_db),
                     current_user: User = Depends(auth_service.get_current_user)):
    cloudinary.config(
        cloud_name=settings.cloudinary_name,
        api_key=settings.cloudinary_api_key,
        api_secret=settings.cloudinary_api_secret,
        secure=True
    )
    public_id = f"Web8/{current_user.id}{current_user.username}"  # generate_folder_name
    r = cloudinary.uploader.upload(file.file, public_id=public_id, owerwrite=True)
    avatar_url = cloudinary.CloudinaryImage(public_id).build_url(width=250, height=250, crop='fill',
                                                                 version=r.get('version'))
    user = await repository_users.update_avatar(current_user.email, avatar_url, db)

    return user

# import hashlib

# def generate_folder_name(user_id: int, email: str) -> str:
#     # Конкатенируем идентификатор и email пользователя в строку
#     user_str = f"{user_id}_{email}"
#     # Применяем хэш-функцию SHA256 для получения уникального имени папки
#     folder_name = hashlib.sha256(user_str.encode('utf-8')).hexdigest()[:12]
#     return folder_name
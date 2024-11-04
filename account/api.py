from ninja import  Router, Query

# router.py
from .models import User
from .schemas import UserCreateSchema, UserUpdateSchema, UserOutSchema
from django.contrib.auth.hashers import make_password
from typing import List
from django.shortcuts import get_object_or_404

from utils.pagination import PaginatedResponseSchema, paginate_queryset

router = Router()

# Create User
@router.post("/users/", response=UserOutSchema)
def create_user(request, payload: UserCreateSchema):
    user = User(
        username=payload.username,
        email=payload.email,
        mobile=payload.mobile,
        alternate_mobile=payload.alternate_mobile,
        role=payload.role,
        password=make_password(payload.password)  # Hash the password
    )
    user.save()
    return user

# Read Users (List)
@router.get("/users/", response=PaginatedResponseSchema)
def users(request,  page: int = Query(1), page_size: int = Query(10)):
    qs = User.objects.all()
    page_number = request.GET.get('page', 1)
    page_size = request.GET.get('page_size', 10)

    return paginate_queryset(request, qs, UserOutSchema, page_number, page_size)

# Read Single User (Retrieve)
@router.get("/users/{user_id}/", response=UserOutSchema)
def retrieve_user(request, user_id: int):
    user = get_object_or_404(User, id=user_id)
    return user

# Update User
@router.put("/users/{user_id}/", response=UserOutSchema)
def update_user(request, user_id: int, payload: UserUpdateSchema):
    user = get_object_or_404(User, id=user_id)
    for attr, value in payload.dict().items():
        if value is not None:
            setattr(user, attr, value)
    user.save()
    return user

# Delete User
@router.delete("/users/{user_id}/")
def delete_user(request, user_id: int):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return {"success": True}

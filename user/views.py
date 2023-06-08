from ninja import Router, Schema

# Authenticate error
from django.contrib.auth import authenticate, login, logout
from ninja.errors import HttpError
from ninja.responses import Response
from ninja.errors import AuthenticationError

from user.schemas import ProfileSchema
from user.models import User, Profile


router = Router(tags=["user"])


class UserCreateSchema(Schema):
    email: str
    username: str
    password: str


class UserLoginSchema(Schema):
    email: str
    password: str


class UserSchema(Schema):
    id = int
    email: str
    username: str


@router.post(
    "/signup",
    response={200: UserSchema},
    auth=None,
)
def post_signup(request, params: UserCreateSchema):
    user = User.objects.create_user(**params.dict())
    return post_login(request, params)


@router.post(
    "/login",
    response={200: UserSchema},
    auth=None,
)
def post_login(request, params: UserLoginSchema):
    user = User.objects.get(email=params.email)

    user = authenticate(request, email=params.email, password=params.password)
    if user is not None:
        login(request, user)
        response = Response(UserSchema.from_orm(user).dict(), status=200, headers={})
        response.set_cookie("sessionid", request.session.session_key)
        return response
    else:
        raise AuthenticationError("Invalid password")


@router.post("/logout")
def post_logout(request):
    logout(request)
    response = Response({"success": True})
    response.delete_cookie("sessionid")
    return response


@router.get("/user", response={200: UserSchema})
def get_user(request):
    return request.user


"""
"""


@router.get("/profile", response={200: ProfileSchema})
def get_profile(request):
    return request.user.profile


@router.post("/profile", response={200: ProfileSchema})
def post_profile(request, params: ProfileSchema):
    profile, _ = Profile.objects.update_or_create(
        user=request.user, defaults=params.dict()
    )
    return profile

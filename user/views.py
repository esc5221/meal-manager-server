from ninja import Router, Schema

# Authenticate error
from django.contrib.auth import authenticate, login, logout
from ninja.errors import HttpError
from ninja.responses import Response
from ninja.errors import AuthenticationError


router = Router(tags=["user"])


from user.models import User


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
    auth=None,
)
def post_signup(request, params: UserCreateSchema):
    user = User.objects.create_user(**params.dict())
    return post_login(request, params)


@router.post(
    "/login",
    auth=None,
)
def post_login(request, params: UserLoginSchema):
    user = User.objects.get(email=params.email)

    user = authenticate(request, email=params.email, password=params.password)
    if user is not None:
        login(request, user)
        response = Response({"success": True})
        response.set_cookie("sessionid", request.session.session_key)
        return response
    else:
        raise AuthenticationError("Invalid password")


@router.post("/logout")
def post_logout(request):
    if request.user.is_authenticated:
        logout(request)
        response = Response({"success": True})
        response.delete_cookie("sessionid")
        return response


@router.get("/user", response={200: UserSchema})
def get_user(request):
    if request.user.is_authenticated:
        return request.user

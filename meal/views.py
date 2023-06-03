from ninja import Router

router = Router()


@router.get("/")
def list_test(request):
    return {"hello": "world"}

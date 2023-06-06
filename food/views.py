from ninja import Router

router = Router()


@router.get("/")
def list_food(request):
    return {"food": "1"}

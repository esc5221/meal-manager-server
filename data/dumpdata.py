import pandas as pd
from food.models import Food, Manufacturer


def float_or_none(value):
    try:
        return float(value)
    except:
        return None


def create_manufacturer(df):
    manufacturer_list = []
    for manufacturer in df["제조사/유통사"].unique():
        if manufacturer == "nan":
            continue
        manufacturer_list.append(Manufacturer(name=manufacturer))

    instances = Manufacturer.objects.bulk_create(
        manufacturer_list, ignore_conflicts=True
    )
    print(len(instances))


def create_food(df):
    manufacturer_list = Manufacturer.objects.all().values_list("id", "name")
    manufacturer_dict = {name: id for id, name in list(manufacturer_list)}

    food_list = []
    for index, row in df.iterrows():
        food_list.append(
            Food(
                db_group=row["DB군"],
                code=row["식품코드"],
                category=row["식품대분류"],
                name=row["식품명"],
                serving_amount=float_or_none(row["1회제공량"]),
                serving_unit=row["내용량_단위"],
                energy=float_or_none(row["에너지(㎉)"]),
                protein=float_or_none(row["단백질(g)"]),
                carbohydrate=float_or_none(row["탄수화물(g)"]),
                sugar=float_or_none(row["총당류(g)"]),
                sodium=float_or_none(row["나트륨(㎎)"]),
                manufacturer_id=manufacturer_dict.get(row["제조사/유통사"]),
            )
        )
    instances = Food.objects.bulk_create(food_list, update_fields=["category"])
    print(len(instances))


def run():
    df = pd.read_csv("data/DB_merged_processed.csv")
    create_manufacturer(df)
    create_food(df)

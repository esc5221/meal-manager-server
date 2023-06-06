def calculate_calories(carbs, protein, fat):
    carb_calories = carbs * 4
    protein_calories = protein * 4
    fat_calories = fat * 9

    total_calories = carb_calories + protein_calories + fat_calories
    return total_calories

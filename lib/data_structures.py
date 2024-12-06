def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]
    

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level_emojis = "🌶" * food['heat_level']
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    # Find the first food that matches the cuisine
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food  # Return the first matching food
    return None  # Return None if no matching food is found

def print_spiciest_foods(spicy_foods):
    # Filter the foods where the heat level is greater than 5
    spiciest_foods = [food for food in spicy_foods if food['heat_level'] > 5]
    
    # Print each of the spiciest foods in the desired format
    for food in spiciest_foods:
        heat_level_emojis = "🌶" * food['heat_level']
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}")

def get_average_heat_level(spicy_foods):
    # check if the list is not empty to avoid division by zero
    if not spicy_foods:
        return 0
    
    # calculate the sum of the heat levels
    total_heat = sum(food['heat_level'] for food in spicy_foods)
    
    # calculate the average heat level
    average_heat = total_heat / len(spicy_foods)
    
    return average_heat

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods  # Return the updated list

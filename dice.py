import random

def roll_dice(dice_number, die_sides):
   
    rolls = []
    for _ in range(dice_number):
        rolls.append(random.randint(1, die_sides))
    return rolls

def calculate_result(rolls, modifier):
    
    return sum(rolls) + modifier

def calculate_stats(dice_number, die_sides, modifier):
    
    min_result = (dice_number * 1) + modifier
    max_result = (dice_number * die_sides) + modifier
    avg_result = (min_result + max_result) / 2
    
    return min_result, avg_result, max_result
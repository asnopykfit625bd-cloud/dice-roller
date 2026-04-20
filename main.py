import dice

def main():
    print("--- Програма-помічник для настільних ігор ---")
    
    try:
        dice_number = int(input("Введіть кількість гральних кісток (наприклад, 3): "))
        die_sides = int(input("Введіть кількість сторін кісток (наприклад, 8): "))
        
        modifier_str = input("Введіть поправку (наприклад, -5 або +2), або 0, якщо її немає: ")
        modifier_str = modifier_str.replace('+', '') # Видаляємо +, якщо користувач його ввів
        modifier = int(modifier_str)
        
        if dice_number < 1 or die_sides < 2:
            print("Помилка: Кількість кісток має бути хоча б 1, а граней — хоча б 2.")
            return

        rolls = dice.roll_dice(dice_number, die_sides)
        result = dice.calculate_result(rolls, modifier)
        min_res, avg_res, max_res = dice.calculate_stats(dice_number, die_sides, modifier)
        

        if modifier > 0:
            mod_display = f"+{modifier}"
        elif modifier < 0:
            mod_display = str(modifier)
        else:
            mod_display = ""
            
        print(f"\nКидок кісток {dice_number}к{die_sides}{mod_display}:")
        print(f"Значення кісток: {rolls}")
        print(f"Результат: {result}")
        
       
        avg_display = int(avg_res) if avg_res.is_integer() else avg_res
        
        print(f"Можливий діапазон [мін., сер., макс.]: [{min_res}, {avg_display}, {max_res}]")

    except ValueError:
        print("Помилка вводу! Будь ласка, вводьте лише цілі числа.")

if __name__ == "__main__":
    main()
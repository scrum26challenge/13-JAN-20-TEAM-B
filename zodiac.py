sign = input("What is your zodiac sign?: ")
mood = input("How are you feeling today?: ")
if sign == 'aries':
    color_pallate = "Red"
elif sign == 'taurus':
    color_pallate = "Black"
elif sign == 'gemini':
    color_pallate = "Light Green"
elif sign == "cancer":
    color_pallate = "Seafoam Green"
elif sign == "leo":
    color_pallate = "Eggplant"
elif sign == 'virgo':
    color_pallate = "Grey"
elif sign == 'libra':
    color_pallate = 'Pastel Pink'
elif sign == 'scorpio':
    color_pallate = "Violet"
elif sign == "sagittarius":
    color_pallate = "Saffron"
elif sign == "capricorn":
    color_pallate = "Grey"
elif sign == "aquarius":
    color_pallate = "Silver"
elif sign == "pices":
    color_pallate = "Peach"
print("Today you should wear: " + color_pallate)

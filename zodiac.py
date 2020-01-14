sign = input("What is your zodiac sign?: ")
mood = input("How are you feeling today?: ")
weather = input("What is the weather today?: ")
if sign == "aries":
    color_pallate = "Red"
elif sign == "taurus":
    color_pallate = "Black"
elif sign == "gemini":
    color_pallate = "Light Green"
elif sign == "cancer":
    color_pallate = "Seafoam Green"
elif sign == "leo":
    color_pallate = "Eggplant"
elif sign == "virgo":
    color_pallate = "Grey"
elif sign == "libra":
    color_pallate = "Pastel Pink"
elif sign == "scorpio":
    color_pallate = "Violet"
elif sign == "sagittarius":
    color_pallate = "Saffron"
elif sign == "capricorn":
    color_pallate = "Grey"
elif sign == "aquarius":
    color_pallate = "Silver"
elif sign == "pices":
    color_pallate = "Peach"

if id >= 800:
    weather_color = "blue"
elif id >= 700:
    weather_color = "white"
elif id >= 600:
    weather_color = "red"
elif id >= 500:
    weather_color = "green"
elif id >= 300 and id < 400:
    weather_color = "yellow"
elif id >= 200 and id < 300:
    weather_color = "purple"
else:
    weather_color = "gray"
print("Today you should wear: " + color_pallate + "based on your zodiac sign / mood.")
print(
    "Today you should wear: " + weather_color + "based on your city's current weather."
)

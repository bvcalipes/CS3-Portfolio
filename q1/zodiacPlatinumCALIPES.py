# List of zodiac signs starting from 1900
zodiacsigns= ["Rat (鼠 / Shǔ)",
    "Ox (牛 / Niú)",
    "Tiger (虎 / Hǔ)",
    "Rabbit (兔 / Tù)",
    "Dragon (龙 / Lóng)",
    "Snake (蛇 / Shé)",
    "Horse (马 / Mǎ)",
    "Goat (羊 / Yáng)",
    "Monkey (猴 / Hóu)",
    "Rooster (鸡 / Jī)",
    "Dog (狗 / Gǒu)",
    "Pig (猪 / Zhū)"]

# Baseline year
BASELINE_YEAR = 1900
birthyear = int(input("Enter your birth year: "))

# Validate user input
if birthyear < BASELINE_YEAR:
    print(f"Invalid Year, it should not be earlier than {BASELINE_YEAR}")
else:
    # Calculate index using modulo arithmetic (12 years cycle)
    zodiac_index = (birthyear - BASELINE_YEAR) % 12
    print(f"Your Chinese Zodiac Sign is: {zodiacsigns[zodiac_index]}")

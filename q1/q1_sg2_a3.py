while True:
    try: 
        year = int(input("Enter your birth year: "))
        if year < 1900:
            print("Invalid year, it should not be earlier than 1900.")
        elif year >= 1900:
            break
    except ValueError:
        print("Invalid input, please enter your birth year ONLY in integers.")
        
year -= 1900

if year % 12 == 0:
    print("Your Chinese Zodiac Sign is : Rat (鼠 / Shǔ)")
elif year % 12 == 1:
    print("Your Chinese Zodiac Sign is : Ox (牛 / Niú)")
elif year % 12 == 2:
    print("Your Chinese Zodiac Sign is : Tiger (虎 / Hǔ)")
elif year % 12 == 3:
    print("Your Chinese Zodiac Sign is : Rabbit (兔 / Tù)")
elif year % 12 == 4:
    print("Your Chinese Zodiac Sign is : Dragon (龙 / Lóng)")
elif year % 12 == 5:
    print("Your Chinese Zodiac Sign is : Snake (蛇 / Shé)")   
elif year % 12 == 6:
    print("Your Chinese Zodiac Sign is : Horse (马 / Mǎ)")       
elif year % 12 == 7:
    print("Your Chinese Zodiac Sign is : Goat (羊 / Yáng)")    
elif year % 12 == 8:
    print("Your Chinese Zodiac Sign is : Monkey (猴 / Hóu)")        
elif year % 12 == 9:
    print("Your Chinese Zodiac Sign is : Rooster (鸡 / Jī)")        
elif year % 12 == 10:
    print("Your Chinese Zodiac Sign is : Dog (狗 / Gǒu)")    
elif year % 12 == 11:
    print("Your Chinese Zodiac Sign is : Pig (猪 / Zhū)")   

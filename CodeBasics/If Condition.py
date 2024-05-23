india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

answer = input("Enter a city name:  ")
answer = answer.lower()
answer2 = input("Enter another City name: ")
answer2 = answer2.lower()

if answer and answer2 in india:
    print("Both Cities is in india")
elif answer and answer2 in pakistan:
    print("Both City is in Pakistan")
elif answer and answer2 in bangladesh:
    print("Both City in bangladesh")
else:
    print(f'They dont belong to the same country')

#----------------Sugar_Levels!---------------//

sugar_level = float(input("Enter your Sugar Level"))

if sugar_level in range(80,100):
    print("Your sugar level is normal ")
elif sugar_level>100:
    print("High Sugar Level")
elif sugar_level<80:
    print("Low Sugar Level")

# სავარჯიშო 1
from itertools import permutations

word = "ABCD"

all_variants = [''.join(p) for p in permutations(word)]

for item in all_variants:
    print(item)

print("სულ რაოდენობა:", len(all_variants))

# სავარჯიშო 2
from datetime import date, timedelta

today = date.today()

days_until_next_monday = (7 - today.weekday()) % 7

if days_until_next_monday == 0:
    days_until_next_monday = 7

next_monday = today + timedelta(days=days_until_next_monday)

first_tuesday = next_monday + timedelta(days=1)

print("მომდევნო კვირის პირველი სამშაბათი:", first_tuesday)
# სავარჯიშო 3
import calendar

myinput = int(input("შეიყვანეთ წელი: "))

if calendar.isleap(myinput):
    print("ნაკიანი წელია")
else:
    print("არ არის ნაკიანი წელი")
# სავარჯიშო 4
from datetime import date

today = date.today()

new_year = date(today.year + 1, 1, 1)

days_left = (new_year - today).days

weeks_left = days_left / 7

print(f"ახალ წლამდე დარჩენილია {weeks_left:.2f} კვირა")
# სავარჯიშო 5
from itertools import combinations

numbers = [1, 2, 3, 4, 5]

result = list(combinations(numbers, 3))

for item in result:
    print(item)
# სავარჯიშო 6
from itertools import combinations

letters = "XYZ"

for length in range(1, len(letters) + 1):
    for combo in combinations(letters, length):
        print("".join(combo))


# სავარჯიშო 7
from datetime import datetime
import random

secret = random.randint(1, 20)

start = datetime.now()
loop = True

while loop:

    finish = (datetime.now() - start).total_seconds()

    if finish > 5:
        print("დრო ამოიწურა, თქვენ დამარცხდით")
        print("სწორი პასუხი იყო:", secret)
        break

    guess = int(input("შეიყვანე რიცხვი (1-20): "))

    if guess == secret:
        print("გილოცავთ, სწორად გამოიცანით")
        loop = False
    else:
        print("არასწორია, სცადეთ თავიდან")
# სავარჯიშო 8
from datetime import datetime, timedelta
import random

start = datetime.now()

player1 = start + timedelta(seconds=random.randint(5, 20))
player2 = start + timedelta(seconds=random.randint(5, 20))

time1 = (player1 - start).total_seconds()
time2 = (player2 - start).total_seconds()

print("Player 1:", time1, "წამი")
print("Player 2:", time2, "წამი")

if time1 < time2:
    print("გაიმარჯვა Player 1")
elif time2 < time1:
    print("გაიმარჯვა Player 2")
else:
    print("ფრე")
# სავარჯიშო 9
from datetime import date

birthday = date(2000, 12, 10)

today = date.today()

next_birthday = date(today.year, birthday.month, birthday.day)

if next_birthday < today:
    next_birthday = date(today.year + 1, birthday.month, birthday.day)

days_left = (next_birthday - today).days

print("შემდეგ დაბადების დღემდე დარჩენილია", days_left, "დღე")
# სავარჯიშო 10
import random
from itertools import product

real_password = ''.join(str(random.randint(1, 6)) for _ in range(4))

print("გენერირებულია ახალი პაროლი")

for password in product('123456', repeat=4):

    attempt = ''.join(password)

    print("ვცდილობ:", attempt)

    if attempt == real_password:
        print("პაროლი სწორია, საცავი გახსნილია")
        print("სწორი პაროლი:", real_password)
        break

# მეორე ვარიანტი
symbols = "0123456789"

with open("mainpass.lst", "w") as f:
    for a in symbols:
        for b in symbols:
            for c in symbols:
                for d in symbols:
                    for e in symbols:
                        f.write(a + b + c + d + e + "\n")

print("mainpass.lst is done")

#  მესამე ვარიანტი ოღონდ არ ვიცი მუშაობს თუ არა

import itertools

symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*-_."
password_length = 8
max_lines_per_file = 1000000
output_file_prefix = "passwords_part"

file_count = 1
line_count = 0
out = open(f"{output_file_prefix}{file_count}.lst", "w")

for combo in itertools.product(symbols, repeat=password_length):
    password = "".join(combo)
    out.write(password + "\n")
    line_count += 1

    if line_count >= max_lines_per_file:
        out.close()
        file_count += 1
        line_count = 0
        out = open(f"{output_file_prefix}{file_count}.lst", "w")

out.close()
print(f"Done! Generated {file_count} output files.")

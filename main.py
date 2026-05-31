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

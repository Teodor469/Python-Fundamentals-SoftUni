# start_year = int(input())
# next_happy_year = start_year + 1


# while True:
#     year_str = str(next_happy_year)
#     if len(year_str) == len(set(year_str)):
#         print(next_happy_year)
#         break
#     next_happy_year += 1

year = int(input())
year_is_special = False
while not year_is_special:
    year += 1
    year_as_string = str(year)
    year_is_special = True
    for digit in year_as_string:
        if year_as_string.count(digit) > 1:
            year_is_special = False
            break
print(year)
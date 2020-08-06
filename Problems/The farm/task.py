user_money = int(input())

PRICE_CHICKEN = 23
PRICE_GOAT = 678
PRICE_PIG = 1296
PRICE_COW = 3848
PRICE_SHEEP = 6769


def print_plural(count, animal):
    plural_animal = f"{animal}s" if (animal != 'sheep' and count > 1) else animal
    print(f"{count} {plural_animal}")


if user_money >= PRICE_SHEEP:
    print_plural(user_money // PRICE_SHEEP, 'sheep')
elif user_money >= PRICE_COW:
    print_plural(user_money // PRICE_COW, 'cow')
elif user_money >= PRICE_PIG:
    print_plural(user_money // PRICE_PIG, 'pig')
elif user_money >= PRICE_GOAT:
    print_plural(user_money // PRICE_GOAT, 'goat')
elif user_money >= PRICE_CHICKEN:
    print_plural(user_money // PRICE_CHICKEN, 'chicken')
else:
    print('None')

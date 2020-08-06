sleep_min = int(input())
sleep_max = int(input())
sleep_curr = int(input())

if sleep_curr < sleep_min:
    print("Deficiency")
elif sleep_curr <= sleep_max:
    print("Normal")
else:
    print("Excess")

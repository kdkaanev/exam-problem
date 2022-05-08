def pirates(d, dp, ep):
    total_plunder = 0.0
    for day in range(1, d + 1):
        total_plunder += dp
        if day % 3 == 0:
            total_plunder += dp / 2
        if day % 5 == 0:
            total_plunder *= 0.7
    if total_plunder >= ep:
        print(f"Ahoy! {total_plunder:.2f} plunder gained.")
    else:
        percentage = total_plunder / ep * 100
        print(f"Collected only {percentage:.2f}% of the plunder.")


days = int(input())
daily_plunder = int(input())
expected_plunder = float(input())

pirates(days, daily_plunder, expected_plunder)
print()
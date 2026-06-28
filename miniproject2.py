cost_per_hour = 0.51

per_day = cost_per_hour * 24
per_week = per_day * 7
per_month = per_day * 30

budget = 918
days = budget / per_day

print("Cost to operate one server per day: $", per_day)
print("Cost to operate one server per week: $", per_week)
print("Cost to operate one server per month: $", per_month)
print("Days one server can operate with $918: ", days)
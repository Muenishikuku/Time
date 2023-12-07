def convert_to_24_hour(hour, minute, period):
    if period == "am":
        if hour == 12:
            hour = 0
    else:  # period is "pm"
        if hour != 12:
            hour += 12

    return f"{hour:02d}{minute:02d}"


# print(convert_to_24_hour(1,00, "pm"))

print(convert_to_24_hour(8, 30, "am"))  # Output: "0830"
print(convert_to_24_hour(8, 30, "pm"))  # Output: "2030"

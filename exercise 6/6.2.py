def convert_temperature(temp, unit):
    if unit == 'C':
        return temp * 9/5 + 32
    elif unit == 'F':
        return (temp - 32) * 5/9
print(f"100°C = {convert_temperature(100, 'C')}°F")
print(f"212°F = {convert_temperature(212, 'F')}°C")
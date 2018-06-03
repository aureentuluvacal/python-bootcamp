print("How many kilometers did you drive today?")
num_kilometers = float(input())
num_miles = round(num_kilometers / 1.60394, 2)

print(f"Ok, you said {num_kilometers} kilometers ({num_miles} miles)")

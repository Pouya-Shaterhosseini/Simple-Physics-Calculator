print("Physics Calculator")
print("1. Velocity (v = d/t)")
print("2. Force (F = m*a)")

choice = input("\nEnter your choice (1 or 2): ")

if choice == "1":
    d = float(input("Enter distance (m): "))
    t = float(input("Enter time (s): "))
    if t == 0:
        print("Error: Time cannot be zero.")
    else:
        print(f"Velocity = {d/t:.2f} m/s")

elif choice == "2":
    m = float(input("Enter mass (kg): "))
    a = float(input("Enter acceleration (m/s²): "))
    print(f"Force = {m*a:.2f} N")

else:
    print("Invalid choice. Please enter 1 or 2.")
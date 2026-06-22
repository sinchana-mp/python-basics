print(" Battery Backup Time Calculator")

voltage = float(input("Enter Battery Voltage (V): "))
ah = float(input("Enter Battery Capacity (Ah): "))
load = float(input("Enter Load Power (W): "))

backup_time = (voltage * ah) / load

print(f"\nEstimated Backup Time = {backup_time:.2f} hours")
land_value = float(input("Enter the land value: "))
years_late = int(input("Enter number of years late: "))
land_use = (input("Enter land use(Residental, Commercial, Agricultural): "))

if land_use =="Residental":
   base_tax = 0.005 * land_value
elif land_use =="Commercial":
   base_tax = 0.01 * land_value
elif land_use =="Agricultural":
   base_tax = 0.002 * land_value
else:
    base_tax = 0
    print("Invalid Land use")

penalty = years_late * 5000

total_due = base_tax + penalty

if years_late == 0:
   status = "No Penalty"
elif years_late ==2:
   status = "Warning Notice"
else:
    status = "Risk of Revocatiom"

print("\n-Land Tax Detail-")
print("Land Value: Naira", land_value)
print("Land Use:", land_use)
print("Base Tax: Naira", base_tax)
print("Status:", status)
print("Total Due:", total_due)
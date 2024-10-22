def get_user_decision():
    while True:
        decision = input("Choose a direction (Left/Right): ").strip().lower()
        if decision in ["left", "right"]:
            return decision
        else:
            print("Invalid input. Please enter 'Left' or 'Right'.")

# Initial locations and their probabilities
locations = [
    {"name": "Location A", "probability": 0.4},
    {"name": "Location B", "probability": 0.3},
    {"name": "Location C", "probability": 0.2},
    {"name": "Location D", "probability": 0.1}
]

# Sort locations by probability in descending order
sorted_locations = sorted(locations, key=lambda x: x["probability"], reverse=True)

decision = get_user_decision()

# Order locations based on user's decision
if decision == "left":
    ordered_locations = sorted_locations
else:  # decision == "right"
    ordered_locations = list(reversed(sorted_locations))

# Print the ordered list of locations
print("\nOrdered list of locations based on your decision:")
for loc in ordered_locations:
    print(f"{loc['name']} - Probability: {loc['probability']}")

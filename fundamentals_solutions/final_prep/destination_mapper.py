import re

all_destinations = input()
valid_destination_pattern = r"(=|\/)([A-Z][A-Za-z]{2,})\1"
# taking only the names
valid_destinations = [destination[1] for destination in re.findall(valid_destination_pattern, all_destinations)]
total_travel_points = sum(len(destination) for destination in valid_destinations)
print("Destinations:", ", ".join(valid_destinations))
print("Travel Points:", total_travel_points)

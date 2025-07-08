countries = input().split(", ")
capitals = input().split(", ")
country_capitals = {country: capital for country, capital in zip(countries, capitals)}

for country, capital in country_capitals.items():
    print(f"{country} -> {capital}")

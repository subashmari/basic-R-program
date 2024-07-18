import math

def option_1():
    # Define the cities and their geographical coordinates (latitude and longitude)
    cities = {
        "Bangalore": (12.9716, 77.5946),
        "Olympic Stadium - Athens, Greece": (37.9715, 23.7269),
        "Wimbledon - London, United Kingdom": (51.4343, -0.2141),
        "Roland Garros (French Open) - Paris, France": (48.8474, 2.2527),
        "Stadio Olimpico - Rome, Italy": (41.9331, 12.4545),
        "Nou Camp - Barcelona, Spain": (41.3809, 2.1228),
        "All England Lawn Tennis and Croquet Club - London, United Kingdom": (51.4343, -0.2141),
        "Mercedes-Benz Arena - Stuttgart, Germany": (48.7914, 9.2323),
        "St. James' Park - Newcastle, United Kingdom": (54.9754, -1.6174),
        "Ibrox Stadium - Glasgow, Scotland": (55.8532, -4.3095),
        "Estádio do Dragão - Porto, Portugal": (41.1622, -8.5856),
        "London, United Kingdom": (51.5072, -0.1276),
        "Paris, France": (48.8566, 2.3522),
        "Rome, Italy": (41.9028, 12.4964),
        "Berlin, Germany": (52.5200, 13.4050),
        "Madrid, Spain": (40.4168, -3.7038),
        "Athens, Greece": (37.9838, 23.7275),
        "Vienna, Austria": (48.2082, 16.3738),
        "Lisbon, Portugal": (38.7223, -9.1393),
        "Amsterdam, Netherlands": (52.3676, 4.9041),
        "Brussels, Belgium": (50.8503, 4.3517),
        "Zermatt, Switzerland (near the iconic Matterhorn)": (45.9764, 7.7481),
        "Interlaken, Switzerland (nestled between Lake Thun and Lake Brienz, with access to the Jungfrau region)": (46.6866, 7.8496),
        "Innsbruck, Austria (Tyrolean Alps)": (47.2692, 11.4069),
        "Salzburg, Austria (near the Berchtesgaden Alps)": (47.8095, 13.0436),
        "Chamonix, France (near Mont Blanc)": (45.9237, 6.8694),
        "Grenoble, France (near the French Alps)": (45.1885, 5.7245)
    }

    cities1={
        "Olympic Stadium - Athens, Greece": (37.9715, 23.7269),
        "Wimbledon - London, United Kingdom": (51.4343, -0.2141),
        "Roland Garros (French Open) - Paris, France": (48.8474, 2.2527),
        "Stadio Olimpico - Rome, Italy": (41.9331, 12.4545),
        "Nou Camp - Barcelona, Spain": (41.3809, 2.1228),
        "All England Lawn Tennis and Croquet Club - London, United Kingdom": (51.4343, -0.2141),
        "Mercedes-Benz Arena - Stuttgart, Germany": (48.7914, 9.2323),
        "St. James' Park - Newcastle, United Kingdom": (54.9754, -1.6174),
        "Ibrox Stadium - Glasgow, Scotland": (55.8532, -4.3095),
        "Estádio do Dragão - Porto, Portugal": (41.1622, -8.5856)
        }
    
    cities2={
        "London, United Kingdom": (51.5072, -0.1276),
        "Paris, France": (48.8566, 2.3522),
        "Rome, Italy": (41.9028, 12.4964),
        "Berlin, Germany": (52.5200, 13.4050),
        "Madrid, Spain": (40.4168, -3.7038),
        "Athens, Greece": (37.9838, 23.7275),
        "Vienna, Austria": (48.2082, 16.3738),
        "Lisbon, Portugal": (38.7223, -9.1393),
        "Amsterdam, Netherlands": (52.3676, 4.9041),
        "Brussels, Belgium": (50.8503, 4.3517)
    }

    # Define the graph as a dictionary with cities as nodes and distances as edges
    graph = {}
    for city1 in cities:
        graph[city1] = {}
        for city2 in cities:
            if city1 != city2:
                # Calculate the distance between cities using Haversine formula
                lat1, lon1 = cities[city1]
                lat2, lon2 = cities[city2]
                R = 6371  # Radius of the Earth in kilometers
                lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
                dlat = lat2 - lat1
                dlon = lon2 - lon1
                a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
                c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
                distance = R * c
                graph[city1][city2] = distance

    def find_nearest_neighbor(city, unvisited_cities):
        min_distance = float('inf')
        nearest_city = None

        for neighbor in unvisited_cities:
            distance = graph[city][neighbor]
            if distance < min_distance:
                min_distance = distance
                nearest_city = neighbor

        return nearest_city, min_distance

    # Initialize a list to store selected cities
    selected_cities = [
        "Zermatt, Switzerland (near the iconic Matterhorn)",
        "Interlaken, Switzerland (nestled between Lake Thun and Lake Brienz, with access to the Jungfrau region)",
        "Innsbruck, Austria (Tyrolean Alps)",
        "Salzburg, Austria (near the Berchtesgaden Alps)",
        "Chamonix, France (near Mont Blanc)",
        "Grenoble, France (near the French Alps)"

    ]

    while len(selected_cities) < 12:
        print("Choose any 6 Sports Places ")
        available_cities = [city for city in cities1.keys() if city not in selected_cities and city != "Bangalore"]
        
        if not available_cities:
            print("No more cities available.")
            break

        for i, city in enumerate(available_cities, start=1):
            print(f"{i}. {city}")

        user_input = input("Enter your choices (e.g., 1, 2, 3): ").strip()
        
        if user_input.lower() == 'q':
            break

        user_choices = user_input.split(',')
        user_choices = [choice.strip() for choice in user_choices]

        for choice in user_choices:
            if choice.isdigit():
                city_index = int(choice) - 1
                if 0 <= city_index < len(available_cities):
                    city_to_add = available_cities[city_index]
                    if city_to_add not in selected_cities:
                        selected_cities.append(city_to_add)
                        
                    else:
                        print(f"{city_to_add} is already in your Itinerary.")
                else:
                    print(f"Invalid number: {choice}. Please enter valid choices.")
            else:
                print(f"Invalid input: {choice}. Please enter only numbers or 'q' to finish selection.")

    while len(selected_cities) < 18:
        print("Choose any 6 captial from below ")
        available_cities = [city for city in cities2.keys() if city not in selected_cities and city != "Bangalore"]
        
        if not available_cities:
            print("No more cities available.")
            break

        for i, city in enumerate(available_cities, start=1):
            print(f"{i}. {city}")

        user_input = input("Enter your choices (e.g., 1, 2, 3): ").strip()
        
        if user_input.lower() == 'q':
            break

        user_choices = user_input.split(',')
        user_choices = [choice.strip() for choice in user_choices]

        for choice in user_choices:
            if choice.isdigit():
                city_index = int(choice) - 1
                if 0 <= city_index < len(available_cities):
                    city_to_add = available_cities[city_index]
                    if city_to_add not in selected_cities:
                        selected_cities.append(city_to_add)
                        
                    else:
                        print(f"{city_to_add} is already in your Itinerary.")
                else:
                    print(f"Invalid number: {choice}. Please enter valid choices.")
            else:
                print(f"Invalid input: {choice}. Please enter only numbers or 'q' to finish selection.")



    # Find the nearest neighbor starting from "Bangalore"
    current_city = "Bangalore"
    optimal_route = [current_city]
    unvisited_cities = [city for city in selected_cities if city != current_city]

    while unvisited_cities:
        nearest_neighbor, min_distance = find_nearest_neighbor(current_city, unvisited_cities)
        optimal_route.append(nearest_neighbor)
        current_city = nearest_neighbor
        unvisited_cities.remove(nearest_neighbor)

    # Calculate the total distance of the route
    total_distance = 0
    for i in range(len(optimal_route) - 1):
        total_distance += graph[optimal_route[i]][optimal_route[i + 1]]

    # Add the distance to return to "Bangalore"
    total_distance += graph[optimal_route[-1]]["Bangalore"]

    # Display the optimal route and its distance
    print("Your travel route :")
    for city in optimal_route:
        print(city)
    print("Total Distance is", total_distance, "km")
    print()

    import matplotlib.pyplot as plt

    # Extract latitude and longitude data for all cities
    city_names = optimal_route
    latitudes = [cities[city][0] for city in city_names]
    longitudes = [cities[city][1] for city in city_names]

    # Create a scatter plot of all cities
    plt.figure(figsize=(12, 8))
    plt.scatter(longitudes, latitudes, c='blue', marker='o', label='Cities')

    # Plot the optimal travel route as lines connecting the cities
    for i in range(len(optimal_route) - 1):
        start_city = city_names[i]
        end_city = city_names[i + 1]
        plt.plot([cities[start_city][1], cities[end_city][1]],
                [cities[start_city][0], cities[end_city][0]], c='red', linestyle='-', linewidth=1)

    # Plot the last leg of the route from the last city back to Bangalore
    plt.plot([cities[optimal_route[-1]][1], cities["Bangalore"][1]],
            [cities[optimal_route[-1]][0], cities["Bangalore"][0]], c='red', linestyle='-', linewidth=1)

    # Add labels for each city
    for i, city in enumerate(city_names):
        plt.annotate(city, (longitudes[i], latitudes[i]), textcoords="offset points", xytext=(0, 10), ha='center')

    # Add a label for Bangalore
    plt.annotate("Bangalore", (cities["Bangalore"][1], cities["Bangalore"][0]), textcoords="offset points", xytext=(0, 10), ha='center')

    # Set axis labels and title
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.title("Optimal Travel Route")

    # Display the plot
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
    

def option_2():
    # Define the cities and their geographical coordinates (latitude and longitude)
    cities = {
        "Bangalore": (12.9716, 77.5946),
        "The Eiffel Tower": (48.8588443, 2.2943506),
        "Louvre Museum": (48.8606111, 2.337644),
        "Palace of Versailles": (48.8048649, 2.1203557),
        "Mont Saint-Michel": (48.636111, -1.511667),
        "Château de Chambord": (47.6162, 1.5113),
        "Notre-Dame Cathedral": (48.8566, 2.3522),
        "The Colosseum": (41.890251, 12.492373),
        "The Vatican": (41.9029, 12.4534),
        "The Pantheon": (41.8986, 12.4768),
        "The Acropolis": (37.9715, 23.7267),
        "Santorini": (36.3932, 25.4284),
        "Plitvice Lakes National Park": (44.8654, 15.6167),
        "Dubrovnik Old Town": (42.6401, 18.1107),
        "Prague Castle": (50.0901, 14.4004),
        "Charles Bridge": (50.0865, 14.4115),
        "The Ringstrasse": (48.2074, 16.3674),
        "Schönbrunn Palace": (48.1852, 16.3129),
        "Vienna State Opera": (48.2025, 16.3681),
        "Matterhorn": (45.9764, 7.6586),
        "Jungfraujoch": (46.5474, 7.9839),
        "Zermatt": (45.9764, 7.7481),
        "Interlaken": (46.6866, 7.8496),
        "Amsterdam Canal Ring": (52.3702, 4.8952),
        "Keukenhof Gardens": (52.2709, 4.5519),
        "Windmills at Kinderdijk": (51.8812, 4.6331),
        "The Alhambra": (37.1760, -3.5886),
        "Park Güell": (41.4144, 2.1527),
        "Sagrada Familia": (41.4036, 2.1744),
        "The Louvre": (48.8606, 2.3376),
        "Versailles Palace": (48.8049, 2.1204),
        "Mont Saint-Michel Abbey": (48.6359, -1.5126),
        "Eiffel Tower": (48.8588, 2.2945),
        "Tower Bridge": (51.5055, -0.0754),
        "The Shard": (51.5045, -0.0865),
        "Buckingham Palace": (51.5014, -0.1419),
        "Stonehenge": (51.1789, -1.8262),
        "Edinburgh Castle": (55.9486, -3.1999),
        "Loch Ness": (57.3229, -4.4244),
        "Giant's Causeway": (55.2408, -6.5116),
        "Cliffs of Moher": (52.9719, -9.4265),
        "Blarney Castle": (51.9291, -8.5702),
        "Prague Astronomical Clock": (50.0875, 14.4214),
        "Český Krumlov Castle": (48.8124, 14.3175),
        "Belvedere Palace": (48.1915, 16.3806),
        "Salzburg Old Town": (47.7994, 13.0458)
    }

    # Function to calculate the Haversine distance between two cities
    def haversine_distance(city1, city2):
        lat1, lon1 = cities[city1]
        lat2, lon2 = cities[city2]

        # Radius of the Earth in kilometers
        R = 6371

        # Convert latitude and longitude from degrees to radians
        lat1 = math.radians(lat1)
        lon1 = math.radians(lon1)
        lat2 = math.radians(lat2)
        lon2 = math.radians(lon2)

        # Haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        distance = R * c

        return distance

    # Initialize a list to store selected cities
    selected_cities = [
    "The Eiffel Tower", "Louvre Museum", "Palace of Versailles", "Mont Saint-Michel", "Château de Chambord",
    "Notre-Dame Cathedral", "The Colosseum", "The Vatican", "The Pantheon", "The Acropolis", "Santorini",
    "Plitvice Lakes National Park", "Dubrovnik Old Town", "Prague Castle", "Charles Bridge", "The Ringstrasse",
    "Schönbrunn Palace", "Vienna State Opera", "Matterhorn", "Jungfraujoch", "Zermatt", "Interlaken",
    "Amsterdam Canal Ring", "Keukenhof Gardens", "Windmills at Kinderdijk", "The Alhambra", "Park Güell",
    "Sagrada Familia", "The Louvre", "Versailles Palace", "Mont Saint-Michel Abbey", "Eiffel Tower",
    "Tower Bridge", "The Shard", "Buckingham Palace", "Stonehenge", "Edinburgh Castle", "Loch Ness",
    "Giant's Causeway", "Cliffs of Moher", "Blarney Castle", "Prague Astronomical Clock", "Český Krumlov Castle",
    "Belvedere Palace", "Salzburg Old Town"
]



    # Function to find the nearest neighbor from a given city
    def find_nearest_neighbor(city, unvisited_cities):
        min_distance = float('inf')
        nearest_city = None

        for neighbor in unvisited_cities:
            distance = haversine_distance(city, neighbor)
            if distance < min_distance:
                min_distance = distance
                nearest_city = neighbor

        return nearest_city, min_distance

    # Calculate the optimal route using the nearest neighbor algorithm
    current_city = "Bangalore"
    optimal_route = [current_city]
    unvisited_cities = [city for city in selected_cities if city != current_city]

    while unvisited_cities:
        nearest_neighbor, min_distance = find_nearest_neighbor(current_city, unvisited_cities)
        optimal_route.append(nearest_neighbor)
        current_city = nearest_neighbor
        unvisited_cities.remove(nearest_neighbor)

    # Calculate the total distance of the route
    total_distance = 0
    for i in range(len(optimal_route) - 1):
        total_distance += haversine_distance(optimal_route[i], optimal_route[i + 1])

    # Add the distance to return to Bangalore
    total_distance += haversine_distance(optimal_route[-1], "Bangalore")

    # Display the optimal route and its distance
    print("Your Travel route ")
    for city in optimal_route:
        print(city)
    print("Total Distance  is ", total_distance, "km")

    import matplotlib.pyplot as plt

    # Extract latitude and longitude data for all cities
    city_names = optimal_route
    latitudes = [cities[city][0] for city in city_names]
    longitudes = [cities[city][1] for city in city_names]

    # Create a scatter plot of all cities
    plt.figure(figsize=(12, 8))
    plt.scatter(longitudes, latitudes, c='blue', marker='o', label='Cities')

    # Plot the optimal travel route as lines connecting the cities
    for i in range(len(optimal_route) - 1):
        start_city = city_names[i]
        end_city = city_names[i + 1]
        plt.plot([cities[start_city][1], cities[end_city][1]],
                [cities[start_city][0], cities[end_city][0]], c='red', linestyle='-', linewidth=1)

    # Plot the last leg of the route from the last city back to Bangalore
    plt.plot([cities[optimal_route[-1]][1], cities["Bangalore"][1]],
            [cities[optimal_route[-1]][0], cities["Bangalore"][0]], c='red', linestyle='-', linewidth=1)

    # Add labels for each city
    for i, city in enumerate(city_names):
        plt.annotate(city, (longitudes[i], latitudes[i]), textcoords="offset points", xytext=(0, 10), ha='center')

    # Add a label for Bangalore
    plt.annotate("Bangalore", (cities["Bangalore"][1], cities["Bangalore"][0]), textcoords="offset points", xytext=(0, 10), ha='center')

    # Set axis labels and title
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.title("Optimal Travel Route")

    # Display the plot
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

def main():
    print("You have got 2 options won in the lucky draw  choose between them:")
    print("1.User can select places from European Continent")
    print("2.Default tourist places from European Continent ")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        option_1()
    elif choice == '2':
        option_2()
    else:
        print("Invalid choice. Please enter 1 or 2.")

  
if __name__ == "__main__":
    main()
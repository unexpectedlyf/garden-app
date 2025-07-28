def get_user_input():
    """
    Get and sanitize user input for season and plant type.
    """
    season = input("Enter the season (e.g., summer, winter): ").strip().lower()
    plant_type = input("Enter the plant type (e.g., flower, vegetable): ").strip().lower()
    return season, plant_type


def generate_advice(season, plant_type):
    """
    Generate gardening advice based on the provided season and plant type.
    """
    advice = ""

    # Advice based on season
    if season == "summer":
        advice += "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        advice += "Protect your plants from frost with covers.\n"
    else:
        advice += "No advice for this season.\n"

    # Advice based on plant type
    if plant_type == "flower":
        advice += "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        advice += "Keep an eye out for pests!"
    else:
        advice += "No advice for this type of plant."

    return advice


def main():
    """
    Main function to drive the gardening advice program.
    """
    season, plant_type = get_user_input()
    advice = generate_advice(season, plant_type)
    print("\nGardening Advice:")
    print(advice)


# Run the program
if __name__ == "__main__":
    main()




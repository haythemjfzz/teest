# Actual week question

actual_week = 22



sunday_times = ["8:00 to 10:00", "10:00 to 12:00", "13:00 to 15:00", "15:00 to 17:00"]



# Monday times question

monday_times = ["8:00 to 10:00", "10:00 to 12:00", "13:00 to 15:00", "15:00 to 17:00"]


# Tuesday times question

tuesday_times = ["8:00 to 10:00", "10:00 to 12:00", "13:00 to 15:00", "15:00 to 17:00"]


# Wednesday times question

wednesday_times = ["8:00 to 10:00", "10:00 to 12:00", "13:00 to 15:00", "15:00 to 17:00"]


# Thursday times question

thursday_times = ["8:00 to 10:00", "10:00 to 12:00", "13:00 to 15:00", "15:00 to 17:00"]

# Friday times question

friday_times = ["8:00 to 10:00", "10:00 to 12:00", "13:00 to 15:00", "15:00 to 17:00"]


# Saturday times question

saturday_times = ["8:00 to 10:00", "10:00 to 12:00", "13:00 to 15:00", "15:00 to 17:00"]


def process_data(data):
    # Extracting values from the received data
    name = data.get("name")
    science_week = int(data.get("s_science_week", 0))
    math_week = int(data.get("s_math_week", 0))
    physic_week = int(data.get("s_physics_week", 0))
    history_week = int(data.get("s_history_week", 0))
    arabic_week = int(data.get("s_arabic_week", 0))
    english_week = int(data.get("s_english_week", 0))
    french_week = int(data.get("s_french_week", 0))
    geography_week = int(data.get("s_geography_week", 0))
    islamic_week = int(data.get("s_islamic_week", 0))

    # Convert to integers safely
    sunday_time = [int(i) for i in (data.get("freetimessunday") or []) if str(i).isdigit()]
    monday_time = [int(i) for i in (data.get("freetimesmonday") or []) if str(i).isdigit()]
    tuesday_time = [int(i) for i in (data.get("freetimesthuesday") or []) if str(i).isdigit()]
    wednesday_time = [int(i) for i in (data.get("freetimeswednesday") or []) if str(i).isdigit()]
    thursday_time = [int(i) for i in (data.get("freetimesthursday") or []) if str(i).isdigit()]
    friday_time = [int(i) for i in (data.get("freetimesfriday") or []) if str(i).isdigit()]
    saturday_time = [int(i) for i in (data.get("freetimessaturday") or []) if str(i).isdigit()]


    # Printing variables for debugging
    print("Processing in softwarS:")
    print(f"Name: {name}")
    print(f"Science Week: {science_week}")
    print(f"Math Week: {math_week}")
    print(f"Physics Week: {physic_week}")
    print(f"History Week: {history_week}")
    print(f"Arabic Week: {arabic_week}")
    print(f"English Week: {english_week}")
    print(f"French Week: {french_week}")
    print(f"Geography Week: {geography_week}")
    print(f"Islamic Week: {islamic_week}")
    print(f"Saturday Week: {saturday_time}")


    
    all_sessions = physic_sessions + math_sessions + arabic_sessions + islamic_sessions + science_sessions + history_sessions + geography_sessions + english_sessions + french_sessions
    import datetime
    def extract_phrases(all_sessions, day_string):
        """Extracts phrases containing the given day_string from all_sessions."""
        return [phrase for phrase in all_sessions if day_string in phrase]
     
    """Processes the received data and returns a modified variable."""



    modified_data = []  # List to store all formatted day data

    # Process all days from 1 to 28
    for day in range(1, 29):
        day_string = f"DAY {day} "
        sessions_phrases = extract_phrases(all_sessions, day_string)

        if sessions_phrases:
            # Format sessions with line breaks instead of commas
            formatted_sessions = "\n".join(sessions_phrases)
            modified_data.append(f"Sessions in {day_string}:\n{formatted_sessions}")
        else:
            modified_data.append(f"No sessions found for {day_string}.")

    # Add additional information at the end
    modified_data.append(f"Additional Time: {additional_time}")
    modified_data.append(f"Total Additional Time Entries: {len(additional_time) if isinstance(additional_time, list) else 1}")

    # Join all processed data with double line breaks for readability
    return {
        "status": "Processed in softwarS",
        "generated_data": "\n\n".join(modified_data)  # Keeps sections separated clearly
    }

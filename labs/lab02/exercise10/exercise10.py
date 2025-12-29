def calculate_base_usage(distance):
    """
    Calculates the base battery usage.
    1.5% battery per 10 meters.
    """
    return (distance/10) * 1.5

def apply_mode_bonus(usage, is_sport_mode):
    """
    Increases battery consumption by 50% if in Sport Mode.
    """
    if is_sport_mode :
        usage = usage + (usage * 0.5)
    else:
        usage = usage + 0

    return usage

def has_enough_battery(distance, current_battery, is_sport_mode):
    """
    Calculates if there is enough battery for a round trip (distance * 2).
    """
    round_trip_distance = distance * 2

    base_usage = calculate_base_usage(round_trip_distance)
    total_usage = apply_mode_bonus(base_usage, is_sport_mode)

    if current_battery >= total_usage:
        return True
    else:
        return False

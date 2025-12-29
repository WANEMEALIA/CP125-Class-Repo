def calculate_xp_required(current_level):
    """
    Calculate XP needed for next level (level * 100).
    """
    return current_level * 100


def can_level_up(current_xp, required_xp):
    """
    Check if player has enough XP to level up.
    """
    if current_xp >= required_xp :
        return True
    else:
        return False


def calculate_final_level(total_xp):
    """
    Calculate the final level reached.
    """
    level = 1
    required_xp = 100

    while total_xp >= required_xp :
        total_xp -= required_xp
        level += 1
        required_xp += 100

    return level


def calculate_remaining_xp(total_xp):
    """
    Calculate XP leftover after leveling.
    """
    level = 1
    xp = total_xp

    while can_level_up(xp, calculate_xp_required(level)):
        xp = xp - calculate_xp_required(level)
        level = level + 1

    return xp

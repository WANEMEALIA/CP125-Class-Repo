def get_legit_power_users(log_data, bot_ids, threshold):
    user_actions = {}

    for time, user_id, action in log_data:
        if user_id not in bot_ids:
            if user_id not in user_actions:
                user_actions[user_id] = set()
            user_actions[user_id].add(action)
    power_users = []
    for user_id in user_actions:
        if len(user_actions[user_id]) > threshold:
            power_users.append(user_id)

    return sorted(power_users)
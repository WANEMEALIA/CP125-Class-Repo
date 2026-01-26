def get_legit_power_users(log_data, bot_ids, threshold):
    user_actions = {}

    for log_data, user_id, threshold in log_data:
        if user_id in bot_ids:
            continue

        if user_id not in user_actions:
            user_actions[user_id] = set()

        user_actions[user_id].add(threshold)
        power_users = []
        
    for user_id, actions in user_actions.items():
        if len(actions) > threshold:
            power_users.append(user_id)

    return sorted(power_users)

def audit_zero_trust(baseline_set, current_log_list):
    current_set = set(current_log_list)

    authorized = baseline_set & current_set
    alerts = current_set - baseline_set
    inactive_authorised = baseline_set - current_set

    return (authorized, alerts, inactive_authorised)
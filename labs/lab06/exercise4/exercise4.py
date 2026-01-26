def synchronize_databases(legacy_list, modern_set, blacklist):
    valid_legacy_ids = set()

    for record_id, email in legacy_list :
        if email not in blacklist :
            valid_legacy_ids.add(record_id)
    lost_ids = valid_legacy_ids - modern_set
    ghost_ids = modern_set - valid_legacy_ids

    return (lost_ids, ghost_ids)
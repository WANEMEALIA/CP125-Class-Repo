def audit_blocklists(list_a, list_b, list_c):
    universal = list_a & list_b & list_c
    redundant = (list_a & list_b) | (list_b & list_c) | (list_a & list_c)
    unique_a = list_a - list_b - list_c

    return(universal, redundant, unique_a)

a, b, c = {"m", "v"}, {"v", "ad"}, {"v", "sp"}
uni, red, uoa = audit_blocklists(a, b, c)
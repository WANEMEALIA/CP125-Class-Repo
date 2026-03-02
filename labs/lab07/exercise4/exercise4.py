def apply_upgrade(current, upgrade):
    updated = current.copy()
    for i in upgrade :
        if i in updated :
            if upgrade[i] > updated[i]:
                updated[i] = upgrade[i]
            else :
                updated[i] = upgrade[i]

    return updated

current = {"read": 2, "write": 1, "admin": 0}
upgrade = {"read": 1, "write": 3, "execute": 2}
result = apply_upgrade(current, upgrade)
print(result)
print(current)   # Should be unchanged

def find_at_risk_departments(departments, threshold):
    at_risk = []
    for i in departments:
        scores = departments[i].values()
        total_students = len(scores)
        below_count = 0

        for i in scores :
            if i < threshold :
                below_count += 1
                
        if below_count > total_students/2:
            at_risk.append(i)
    return sorted(at_risk)

departments = {
    "CS":      {"Ali": 85, "Sara": 55, "Zaki": 62},
    "Math":    {"Hana": 90, "Reza": 88},
    "English": {"Tom": 45, "Jay": 50, "Lin": 48},
}
print(find_at_risk_departments(departments, 65))

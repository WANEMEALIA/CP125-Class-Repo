def match_specialists(candidates_list, project_requirements):
    skill_count = {}

    for name,skills in candidates_list :
        for i in skills:
            if i not in skill_count :
                skill_count[skill]

def add_viewer(person, team=None):
    team = team if team is not None else []
    team.append(person)
    return team

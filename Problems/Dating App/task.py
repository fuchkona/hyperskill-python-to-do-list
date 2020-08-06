def select_dates(potential_dates):
    names = []
    for human in potential_dates:
        if human['age'] > 30 \
                and 'art' in human['hobbies'] \
                and human['city'] == 'Berlin':
            names.append(human['name'])
    return ', '.join(names)

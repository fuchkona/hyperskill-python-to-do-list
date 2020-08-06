def tallest_people(**people):
    tallest_height = max(*people.values())
    tallest_names = []
    for name, height in people.items():
        if height == tallest_height:
            tallest_names.append(name)
    tallest_names = sorted(tallest_names)
    for name in tallest_names:
        print(f"{name} : {tallest_height}")

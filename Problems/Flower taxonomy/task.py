iris = {}


def add_iris(id_n, species, petal_length, petal_width, **kwargs):
    global iris
    data = {
        'species': species,
        'petal_length': petal_length,
        'petal_width': petal_width,
    }

    for key, value in kwargs.items():
        data[key] = value

    iris[id_n] = data

def run():
    my_list = [1, 'hello', True, 4.5]  # listas
    my_dict = {'firstname': 'giovany', 'lastname': 'osorio'}  # diccionario

    super_list = [
        {'firstname': 'giovany', 'lastname': 'osorio'},
        {'firstname': 'miguel', 'lastname': 'torres'},
        {'firstname': 'andres', 'lastname': 'trujillo'},
        {'firstname': 'pepe', 'lastname': 'martinez'},
        {'firstname': 'marcos', 'lastname': 'barretini'}
    ]  # lista de diccionarios

    super_dict = {
        'natural_nums': [1, 2, 3, 4, 5],
        'integer_nums': [-1, -2, 0, 1, 2],
        'floating_nums': [1.1, 2.4, 3.5, 4.5, 5.5],

    }    # diccionario de listas
    # comprobamos que un diccionario puede tener listas

    for key, value in super_dict.items():
        print(key, "-", value)


if __name__ == '__main__':
    run()

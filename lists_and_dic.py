def run():
    my_list = [1, "hello", True, 4.6]
    my_dict = {"firstname": "Ulises", "lastname": "Mejia"}

    super_list = [
        {"firstname": "Ulises", "lastname": "Mejia"},
        {"firstname": "Michelle", "lastname": "Castillo"},
        {"firstname": "Veronica", "lastname": "Mejia"},
        {"firstname": "Tina", "lastname": "Mejia"}
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-2, -1, 0, 1, 2],
        "floating_nums": [1.2, 5.6, 8.6, 9.0]
    }

    for key, value in super_dict.items():
        print(key, "-", value)

    for i in super_list:
	    print(i.items())   



if __name__ == "__main__":
    run()
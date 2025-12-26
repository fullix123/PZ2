from calculations import FUNCTIONS
from visualization import print_table, plot_graph


def generate_range(a, b, step):
    values = []
    x = a
    while x <= b:
        values.append(x)
        x += step
    return values


def main():
    print("Выберите функцию:")
    for key, (name, _) in FUNCTIONS.items():
        print(f"{key}. {name}")

    choice = input("Введите номер функции: ")
    func_name, func = FUNCTIONS[choice]

    a = float(input("Введите a: "))
    b = float(input("Введите b: "))
    step = float(input("Введите шаг: "))

    x_values = generate_range(a, b, step)
    y_values = []

    for x in x_values:
        try:
            y_values.append(func(x))
        except Exception as e:
            print(f"Ошибка при x={x}: {e}")
            y_values.append(None)

    print_table(x_values, y_values)
    plot_graph(x_values, y_values, func_name)


if __name__ == "__main__":
    main()

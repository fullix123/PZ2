import matplotlib.pyplot as plt


def print_table(x_values, y_values, precision=3):
    print("\nТаблица значений:")
    print("X:", end=" ")
    for x in x_values:
        print(f"{x:.{precision}f}", end=" ")
    print("\nY:", end=" ")
    for y in y_values:
        print(f"{y:.{precision}f}", end=" ")
    print("\n")


def plot_graph(x_values, y_values, title="График функции"):
    plt.plot(x_values, y_values)
    plt.title(title)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()

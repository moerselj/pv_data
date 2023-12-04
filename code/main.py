import inquirer


def main():
    selected_unit = inquirer.list_input("Metric or imperial?", choices=['metric', 'imperial'])
    print(selected_unit)


if __name__ == "__main__":
    main()

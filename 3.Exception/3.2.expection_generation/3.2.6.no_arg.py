def read_file(file_path):
    try:
        with open(file_path, "r") as file:
            data = file.read()
            if not data:
                raise RuntimeError
            return data
    except FileNotFoundError:
        print("Файл не найден.")
    except RuntimeError:
        print("Ошибка чтения файла.")


read_file("example.txt")

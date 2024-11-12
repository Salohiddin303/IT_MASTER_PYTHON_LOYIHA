def print_first_three_lines(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            # Fayldan dastlabki uch qatorni o'qish
            for i in range(3):
                line = file.readline()
                if line:
                    print(line.strip())
                else:
                    break
    except FileNotFoundError:
        print(f"{filename} fayli topilmadi.")

    
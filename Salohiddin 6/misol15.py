def file_statistics(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            # Qatorlar soni
            line_count = len(lines)

            # So'zlar soni
            word_count = sum(len(line.split()) for line in lines)

            # Bo'sh joy va belgilar soni
            space_char_count = sum(line.count(' ') + line.count('\t') for line in lines)

            # Natijani chiqarish
            print(f"Количество строк в файле {filename}: {line_count}")
            print(f"Количество слов: {word_count}")
            print(f"Число символов: {space_char_count}")

    except FileNotFoundError:
        print(f"{filename} fayli topilmadi.")



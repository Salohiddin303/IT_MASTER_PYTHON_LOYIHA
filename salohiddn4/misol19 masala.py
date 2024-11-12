# O'zbekcha -> Ruscha lug'at
uz_to_ru = {
    'salom': 'privet',
    'dunyo': 'mir',
    'kitob': 'kniga',
    'uy': 'dom',
    'ota': 'otets',
    'ona': 'mat',
    'maktab': 'shkola'
}

# Ruscha -> O'zbekcha lug'at
ru_to_uz = {
    'privet': 'salom',
    'mir': 'dunyo',
    'kniga': 'kitob',
    'dom': 'uy',
    'otets': 'ota',
    'mat': 'ona',
    'shkola': 'maktab'
}


# Asosiy dastur funksiyasi
def translate():
    while True:
        print("1 - Uz -> Ru")
        print("2 - Ru -> Uz")
        choice = input("Tanlang (1 yoki 2): ")

        if choice == '1':
            word = input("So'z kiriting (O'zbekcha): ").lower()
            if word in uz_to_ru:
                print(f"Tarjimasi: {uz_to_ru[word]}")
            else:
                print("So'z lug'atda topilmadi.")

        elif choice == '2':
            word = input("Insert word (Russian): ").lower()
            if word in ru_to_uz:
                print(f"Translation: {ru_to_uz[word]}")
            else:
                print("Word not found in the dictionary.")

        else:
            print("Noto'g'ri tanlov qildingiz, iltimos qaytadan kiriting.")

        # Yana davom etish uchun foydalanuvchidan so'rash
        cont = input("Davom etishni xohlaysizmi? (ha/yo'q): ").lower()
        if cont != 'ha':
            break


# Dastur ishga tushirilishi
translate()
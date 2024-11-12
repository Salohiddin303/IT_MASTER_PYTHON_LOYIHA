def find_negative_range(lst):
    # Birinchi va oxirgi manfiy elementlarning indekslarini topish
    first_neg_idx = -1
    last_neg_idx = -1

    for i in range(len(lst)):
        if lst[i] < 0:
            if first_neg_idx == -1:
                first_neg_idx = i  # Birinchi manfiy element
            last_neg_idx = i  # Oxirgi manfiy element


    if first_neg_idx != -1 and last_neg_idx != -1:

        return lst[first_neg_idx:last_neg_idx + 1]
    else:
        return []


# Sinov uchun
lst = [2, 33, -4, 5, 4, 88, 7, 22, -4, 55, 4, 99, -6, 88, 9, 2, 33]
result = find_negative_range(lst)
print(result)
st='12 31 4 53 6 7 4 90 8 7 56 3 42'
my_dict={n: int(n) * 2
         for n in st.split()
         if int(n) % 2 == 0}
print(my_dict)
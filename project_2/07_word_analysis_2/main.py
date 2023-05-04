word = input("Введите слово: ")
list_word = list(word)
index = len(list_word)

x = 0
count = 0
for i in range(index // 2):
    if list_word[i] == list_word[index - 1 - x]:
        count += 1
    x += 1
if count == index // 2:
    print(f"Слово {word} является палиндромом.")
else:
    print(f"Слово {word} не является палиндромом.")
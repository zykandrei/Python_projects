count_video_cards = int(input('Количество видеокарт: '))
old_list_cards = []
new_list_cards = []
for i in range(1, count_video_cards + 1):
    video_cards = int(input(f'{i} Видеокарта: '))
    old_list_cards.append(video_cards)
print('Старый список видеокарт: ', old_list_cards)

if old_list_cards:
    max_num_card = old_list_cards[0]
    for max_card in old_list_cards:
        if max_num_card < max_card:
            max_num_card = max_card
    for j in old_list_cards:
        if j != max_num_card:
            new_list_cards.append(j)

    print('Новый список видеокарт: ', new_list_cards)
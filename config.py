TOKEN = '1203682284:AAFEsdp57qJQr4CXDIpLkUOhohK1ePvqpCQ'
commands = {
    '▫🏦/banktime': 'Через сколько банки будут собирать процент по кредиту',
    '▫🏦/getcredit': 'Взять кредит в банке',
    '▫🏦/paytobank': 'Отправить деньги банку',
    '▫🏦/newbank': 'Создать свой банк',
    '▫🏦/setbank': 'Изменить свой банк',
    '▫🏦/mybank': 'Статистика вашего банка',
    '▫🏦/bank_info': 'Посмотреть инфо о банке',
    '▫🏦/banks': 'Список банков',
    '▫⏱/uptime': 'Время работы и проверка бота',
    '▫🦠/corona': 'Онлайн статистика COVID-19 в мире',
    '▫🦠/corona_ru': 'Онлайн статистика COVID-19 в РФ',
    '▫🦠/corona_uk': 'Онлайн статистика COVID-19 в Украине',
    '▫💶/prices': 'Цены в боте',
    '▫💶/balance': 'Посмотреть свой баланс',
    '▫💶/payto': 'Отправить деньги пользователю',
    '▫🐕/buy_pet': 'Купить питомца',
    '▫🐕/mypets': 'Список моих питомцев',
    '▫🐕/pet': 'Показать ифно о питомце',
    '▫🐕/pet_setavatar': 'Установить питомцу новый аватар',
    '▫🐕/pet_setname': 'Установить питомцу новое имя',
    '▫🎰/rullet': 'Играть в рулетку',
    '▫🎰/rullet_bank': 'Узнать сколько слито в рулетку',
    '▫🧾/admin_list': 'Список админов бота',
    '▫🧾/total_messages': 'Количество сообщений от юзеров',
    '▫🧾/banlist': 'Узнать кто посасывает бибу',
    '▫📈/my_stat': 'Показать свою статистику',
    '🔸🍓/showgif': 'Показать 18+ гифку',
    '🔸🍓/showpic': 'Показать 18+ картинку',
    '🔸📈/stat_for': 'Показать статистику пользователя',
    '🔸🛠/add_admin': 'Добавить пользователя в админы бота ',
    '🔸☠/ban_user': 'Забанить пользователя ️',
    '🔸🚫/unban_user': 'Разбанить пользователя ',
    '🔺❗/set':'Установить значение БД для пользователя',
    '🔺🛠/del_admin':'Удалить пользователя из админов бота ',
}

global_economic = {
    "bank_cost" : 300000, # Стоимость покупки питомца
    "pet_cost" : 3000, # Стоимость покупки питомца
    "pet_food_cost" : 2, # Стоимость покупки 1 еды
    "pet_water_cost" : 2, # Стоимость покупки 1 воды
    "pet_house_cost" : 700, # Стоимость покупки дома
    "pet_house_cost_multiplier" : 1, # Множитель стоимости дома, меняется от уровня дома
    "pet_change_avatar_cost" : 100, # Стоимость смены аватара
    "pet_change_name_cost" : 50, # Стоимость смены имени
    "pet_unique_treasure_sell_cost" : 1000, # Стоимость обмена найденных сокровищ на деньги
    "slot_jackpot" : 9000, # Джекпот в рулетке
    "slot_jackpot_multiplier" : 1, # Множитель джекпота
    "slot_earned_from_users" : 0, # Сколько рулетка заработала на пользователях
    "slot_payed_to_users" : 0, # Сколько рулетка выплатила пользователям
    "slot_spin_cost" : 200, # Стоимость одного вращения рулетки, т.е. ставка
    "slot_item1_cost" : 200, # Цена за 1-й предмет рулетки
    "slot_item2_cost" : 250, # Цена за 2-й предмет рулетки
    "slot_item3_cost" : 350, # Цена за 3-й предмет рулетки
    "slot_item4_cost" : 600, # Цена за 4-й предмет рулетки
    "slot_item5_cost" : 100000 # Цена за 5-й предмет рулетки
}

global_economic_desc = {
    "🏦Банк" : "100к 💶. Создать свой банк",
    "🐕Питомец" : "3000💶 (P*C). Где P = цена, C = количество купленных питомцев", # Стоимость покупки питомца
    "🍗Еда" : "2💶", # Стоимость покупки 1 еды
    "💧Вода" : "2💶", # Стоимость покупки 1 воды
    "🏠Покупка дома" : "700💶", # Стоимость покупки дома
    "⚙🐕️Смена аватара" : "100💶", # Стоимость смены аватара
    "⚙🐕️Смена имени" : "50💶", # Стоимость смены имени
    "💎Стоимость сокровищ" : "1000💶", # Стоимость обмена найденных сокровищ на деньги
    "🎰Одно вращение рулетки" : "200💶"
}



bank = {
    "id" : "0", # Имя пользователя
    "money": 10000, # Деньги банка
    "time_to_grab_percent_m": 60, # Время через сколько собирать процент по кредиту у пользователей которые его взяли
}
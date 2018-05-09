# ДЗ-1
# исходную информацию по квартирам можно взять по этой ссылке или придумать самим
# https://www.cian.ru/cat.php?currency=2&deal_type=sale&engine_version=2&foot_min=20&ipoteka=1&maxprice=3500000&offer_type=flat&only_foot=2&region=1&room1=1&room2=1&sost_type%5B0%5D=1

# информация о квартирах вложенным списком
# стоимость, кол-во комнат, пешком до метро (мин), построена/строится

# TODO1: добавить в список flats параметры квартиры: этаж, наличие лифта ("да"/"нет")
flats = [[3189226, 1, 11, "построена"], [3500000, 1, 9, "построена"], [3200000, 1, 20, "построена"], \
         [3300000, 1, 8, "построена"], [3400000, 1, 20, "построена"], [3400000, 1, 2, "построена"], \
         [2999000, 2, 16, "построена"], [3490000, 1, 4, "построена"], [2999000, 1, 6, "построена"], \
         [2759730, 1, 1, "строится"], [2369234, 1, 10, "строится"]]

# TODO2: в коде ниже дописать сложный фильтр подбора квартир для пожилых людей: показать все уже построенные квартиры, не дальше 15 мин пешком от метро, и либо на первом этаже, либо в доме, где есть лифт. Попробуйте использовать не только and, но и not и or
for i, flat in enumerate(flats):
    if "построена" in flat[3] and flat[2] <= 15:
        print(("{0}. {1}").format(i, str(flat)))

# дз:
# 1) Добавьте параметры в описание квартиры и сделайте сложный фильтр. См. TODO1, TODO2
# Исходные данные можете придумать самостоятельно или взять из таблицы эксель по ссылке:
# https://goo.gl/yotH24

# 2) Подумайте и расскажите, какие ваши повседневные действия лучше всего
# описываются циклом for, а какие - while.

# 3) Напишите программу на python, которая "выполняет" вот этот анекдот:
# Идет по улице прохожий, смотрит - на газоне двое рабочих. Первый выкапывает яму,
# ждут, второй закапывает. Перекур. Потом все повторяется.
# Прохожий не выдерживает: "Мужики, а что вы делаете-то?"
# Ну понимаешь, вообще мы деревья сажаем. Я выкапываю яму, Петрович кладет туда саженец,
# Серега закапывает. А сегодня Петрович заболел...
# 3.1) Написать "правильный" цикл, как сажают деревья.
# Выход из цикла - по окончании рабочего дня. Сколько у рабочих было саженцев - мы не знаем.
# 3.2) Сделать так, что Петрович заболел: добавить условие по вводу с клавиатуры. Совет: используйте цикл while.

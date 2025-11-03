from operator import itemgetter

class HDD:
    """Жесткий диск"""
    def __init__(self, id, name, capacity, comp_id):
        self.id = id
        self.name = name
        self.capacity = capacity
        self.comp_id = comp_id

class Comp:
    """Компьютер"""
    def __init__(self, id, name):
        self.id = id
        self.name = name

class HDDComp:
    """
    'Жесткий диск компьютера' для реализации
    связи многие-ко-многим
    """
    def __init__(self, comp_id, hdd_id):
        self.comp_id = comp_id
        self.hdd_id = hdd_id

# Компьютеры
comps = [
    Comp(1, 'ПК Иванова'),
    Comp(2, 'ПК Петрова'),
    Comp(3, 'Сервер компании'),
    Comp(4, 'ПК Сидорова'),
    Comp(5, 'Гостевой компьютер')
]

# Жесткие диски
HDDs = [
    HDD(1, 'Seagate Barracuda 7200', 320, 1),
    HDD(2, 'Western Digital WD Blue', 1024, 4),
    HDD(3, 'Barracuda 7200rpm', 2048, 1),
    HDD(4, 'WD Purple WD64PURZ', 6144, 3),
    HDD(5, 'Toshiba DT01', 1024, 2),
    HDD(6, 'Blue WD20EZBX', 2048, 5),
    HDD(7, 'Western Digital WD Caviar Blue', 4096, 2)
]

HDDs_comps = [
    HDDComp(1, 1),
    HDDComp(1, 3),
    HDDComp(2, 5),
    HDDComp(2, 7),
    HDDComp(3, 4),
    HDDComp(4, 2),
    HDDComp(5, 6),
]

def main():
    one_to_many = [(d.name, d.capacity, c.name)
        for d in HDDs
        for c in comps
        if d.comp_id == c.id
        ]

    many_to_many_temp = [(c.name, dc.comp_id, dc.hdd_id)
        for c in comps
        for dc in HDDs_comps
        if c.id == dc.comp_id
    ]

    many_to_many = [(d.name, d.capacity, comp_name)
        for comp_name, comp_id, hdd_id in many_to_many_temp
        for d in HDDs if  d.id == hdd_id
    ]

    print('Задание 1')
    res_1 = sorted(one_to_many, key = itemgetter(0))
    print(res_1)

    print('Задание 2')
    res_2_unsorted = []
    for c in comps:
        disks_in_comps = list(filter(lambda x: x[2] == c.name, one_to_many))
        count = len(disks_in_comps)
        if count > 0:
            res_2_unsorted.append((c.name, count))
    res_2 = sorted(res_2_unsorted, key = itemgetter(1))
    for comp, cnt in res_2:
        print(f'Компьютер: {comp}, количество жестких дисков: {cnt}')

    print('Задание 3')
    res_3 = [
        (hdd_name, comp_name)
        for hdd_name, capacity, comp_name in many_to_many
        if hdd_name.endswith("Blue")
    ]
    res_3_unique = list(set(res_3))
    if res_3_unique:
        print('Диски, названия которых заканчивается на "Blue":')
        for hdd, comp in sorted(res_3_unique):
            print(f'Жёсткий диск: {hdd}, компьютер: {comp}.')
    else:
        print('Нет жестких дисков, названия которых заканчивается на "Blue".')

if __name__ == "__main__":
    main()

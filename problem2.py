import csv


def read_row(row):
    """Считывает строку и возращает обработанный словарь

    Параметры:
    row -- строка
    """
    return {"id": int(row[0]),"Name":row[1],"titleProject_id":int(row[2]),"class":row[3],"score":(int(row[4]) if row[4] != "None" else None)}

def read_file(filename):
    """Считывает данные и возращает лист словарей

    Параметры:
    filename -- имя файла
    """

    result = []
    header = True
    with open(filename, encoding="utf8") as f:
        for row in csv.reader(f):
            if header:
                header = False
                continue
            result.append(read_row(row))
    
    return result

def average_score(data, cls):
    """Возвращает среднюю оценку за проекты по классу

    Параметры:
    data -- основная таблица
    cls -- класс
    """
    sm = l =0
    for d in data:
        if d["score"] != None and d["class"] == cls:
            sm+=d["score"]
            l+=1
    return sm/l

def repair_table(data):
    """Исправляет таблицу-словарь
    
    Параметры:
    data -- основная таблица
    """
    for d in data:
        if d["score"] == None: d["score"] = round(average_score(data, d["class"]), 3)

def insertion_sort(arr, key=lambda x: x):
    """Сортирует массив алгоритмом вставками
    
    Параметры:
    arr - массив
    key - ключ сортировки
    """

    for i in range(len(arr)):
        j = i
        x= arr[i]

        while j>0 and key(x) < key(arr[j-1]):
            arr[j] = arr[j-1]
            j-=1
        
        arr[j] = x
    
def get_10(data):
    """Выдаёт словари учеников 10 ых классов
    
    Параметры:
    data -- основная таблица
    """
    result = []
    for d in data:
        if d["class"][:2] == "10":
            result.append(d)
    return result
    


if __name__ == "__main__":
    table = read_file("students.csv")
    repair_table(table)
    insertion_sort(table, key=lambda x: x["score"])
    table10 = get_10(table)
    
    print("10 класс:")
    for i in range(1, 4):
        name = table10[-i]["Name"].split()

        print(f"{i} место: {name[1][0]}. {name[0]}")

    

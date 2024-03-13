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

def find_score(data, name):
    """Ищет оценку, которую получил ученик, и id проекта

    Параметры:
    name -- имя ученика
    data -- основная таблица
    """

    for d in data:
        if d['Name'] == name: return (d["titleProject_id"], d["score"])


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

def write_file(data, filename):
    """Записывает таблицу-словарь в новый файл
    
    Параметры:
    data -- основная таблица
    filename -- имя файла
    """
    with open(filename, "w", encoding="utf8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id","Name","titleProject_id","class","score"])
        writer.writerows([list(x.values()) for x in data])

if __name__ == "__main__":
    table = read_file("students.csv")
    id, score = find_score(table, "Хадаров Владимир Валериевич")
    print(f"Ты получил: {score}, за проект - {id}")

    repair_table(table)
    write_file(table, "student_new.csv")
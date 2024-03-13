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

def gen_hash(d):
    """генерирует хеш для одной строки в таблице
    
    Параметры:
    d -- строка таблицы
    """
    name = [ord(x) for x in d["Name"]]
    p = 67
    m = 10e9+9
    return int(sum([(name[x]*(p**x))%m for x in range(len(name))]))

def reform_table(data):
    """Заменяет значения в столбце id на значение хеша
    
    Параметры:
    data -- основная таблица
    """
    for d in data:
        d["id"] = gen_hash(d)
    

def write_file(data, filename):
    """Записывает таблицу-словарь в новый файл
    
    Параметры:
    data -- основная таблица
    filename -- имя файла
    """
    with open(filename, "w", encoding="utf8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id","Name","titleProject_id","class","score","username","password"])
        writer.writerows([list(x.values()) for x in data])



if __name__ == "__main__":
    table = read_file("students.csv")
    reform_table(table)
    write_file(table, "students_with_hash.csv")
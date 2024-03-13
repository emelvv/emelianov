import csv
import random


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

def gen_pass_login(d):
    """Генерирует пароль и логин для строки
    
    Параметры:
    d -- строка из таблицы
    """
    alph = "0123456789"+"".join([chr(x) for x in range(65, 91)])+"".join([chr(x) for x in range(65, 91)]).lower()
    pas = "".join([alph[random.randint(0, len(alph)-1)] for _ in range(8)])
    name = d['Name'].split()
    usr = f"{name[0]}_{name[1][0]}{name[2][0]}"
    return usr, pas

def add_cred(data):
    """Добавляет в таблицу-словарь два новых столбца username и password
    
    Параметры:
    data -- основная таблица
    """
    for d in data:
        usr, pas = gen_pass_login(d)
        d["username"], d["password"] = usr, pas

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
    add_cred(table)
    write_file(table, "students_password.csv")
    

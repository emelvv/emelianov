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

def find_score(data, id):
    """Ищет оценку, которую получил ученик, и его имя

    Параметры:
    id -- id проекта
    data -- основная таблица
    """

    for d in data:
        if d['titleProject_id'] == id: return (d["Name"], d["score"])

    return None


if __name__ == "__main__":
    table = read_file("students.csv")
    while True:
        id = input("\nВведите номер проекта: ")
        if id == "СТОП": break
        id = int(id)

        res = find_score(table, id)
        if res == None:
            print("Ничего не найдено.")
        else:
            name, score = res
            name = name.split()
            print(f"Проект № {id} делал: {name[1][0]}.{name[0]} он(а) получил(а) оценку - {score}.")

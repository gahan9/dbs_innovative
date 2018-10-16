import os
from collection.models import Title
from moviedb.settings import BASE_DIR


def add_data():
    FILE_PATH = os.path.join(BASE_DIR, "dump", "data.tsv")
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r', encoding="utf-8") as f:
            content = f.read()
        data = content.split("\n")
        for val in data[1000:]:
            row = [i.replace("\\N", "").strip() if i.replace("\\N", "").strip() else None for i in val.split("\t")]
            # print(row)
            # try:
            #     ordering = int(val[1])
            # except ValueError:
            #     ordering = 1000
            row_dict = {
                "title_id": row[0],
                "ordering": int(row[1]),
                "title": row[2],
                "region": row[3],
                "language": row[4],
                "types": row[5],
                "attributes": row[6],
                "is_original_title": bool(row[7]),
            }
            # print(row_dict)
            Title.objects.get_or_create(**row_dict)
    else:
        print("Path not exist")


if __name__ == "__main__":
    add_data()

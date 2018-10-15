import os
from collection.models import Title
from moviedb.settings import BASE_DIR


def add_data():
    FILE_PATH = os.path.join(BASE_DIR, "dump", "data.tsv")
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r', encoding="utf-8") as f:
            content = f.read()
        data = content.split("\n")
        for val in data[1:10]:
            row = [i.replace("\\N", "").strip() if i.replace("\\N", "").strip() else None for i in val.split("\t")]
            row_dict = {
                "title_id": val[0],
                "ordering": val[1],
                "title": val[2],
                "region": val[3],
                "language": val[4],
                "types": val[5],
                "attributes": val[6],
                "is_original_title": val[7],
            }
            Title.objects.get_or_create(**row_dict)
    else:
        print("Path not exist")


if __name__ == "__main__":
    add_data()

import os
import sys
from threading import Thread
from itertools import islice

from django.db import DataError

from collection.models import Title
from moviedb.settings import BASE_DIR

DATA_LEN = 3671031


def generate_data():
    FILE_PATH = os.path.join(BASE_DIR, "dump", "data.tsv")
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r', encoding="utf-8") as f:
            content = f.read()
        data = content.split("\n")
        DATA_RANGE_SKIP = Title.objects.count()
        for val in data[DATA_RANGE_SKIP:]:
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
            return row_dict
            # print(row_dict)
            # try:
            #     Title.objects.get_or_create(**row_dict)
            # except DataError:
            #     print("Error for below entry:\n{}".format(row_dict))
    else:
        print("Path not exist")


def add_data_to_db(batch_size=500):
    DATA_RANGE = DATA_LEN - Title.objects.count()
    objects = (Title(generate_data()) for i in range(min(1000, DATA_RANGE)))
    while True:
        batch = list(islice(objects, batch_size))
        if not batch:
            break
        Title.objects.bulk_create(batch, batch_size)


if __name__ == "__main__":
    add_data_to_db()

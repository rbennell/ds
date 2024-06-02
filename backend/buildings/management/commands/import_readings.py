from typing import Dict, List
from django.core.management.base import BaseCommand
from buildings.models import Building, Reading
import csv
from django.db import transaction


def read_file(building_name: str):
    filename = f"buildings_data/{building_name}.csv"
    data = []
    print("reading data!")
    with open(filename, "r") as inf:
        csv_reader = csv.DictReader(inf)
        for r in csv_reader:
            data.append(r)
    print(data)
    return data


@transaction.atomic  # this ensures if anything fails we don't save anything to the db!
def add_data_for_building(building_name: str, data: List[Dict]):
    print("creating building!")
    building = Building.objects.create(name=building_name)
    print("creating readings")
    Reading.objects.bulk_create(
        [
            Reading(
                building=building, date=row["date"], reading=float(row["reading"][:-3])
            )
            for row in data
        ]
    )
    print(f"finished adding building {building_name}")


class Command(BaseCommand):
    help = "Imports the specified file in to the db"

    def add_arguments(self, parser):
        parser.add_argument("building_name", type=str)

    def handle(self, *args, **options):
        building_name = options["building_name"]
        data = read_file(building_name)
        add_data_for_building(building_name, data)

from django.core.management.base import BaseCommand, CommandError
from buildings.models import Building, Reading
import csv


def read_file(building_name: str):
    filename = f"buildings_data/{building_name}.csv"
    with open(filename, "r") as inf:
        csv_reader = csv.reader(inf)
        for r in csv_reader:
            print(r)


class Command(BaseCommand):
    help = "Imports the specified file in to the db"

    def add_arguments(self, parser):
        parser.add_argument("building_name", type=str)

    def handle(self, *args, **options):
        building_name = options["building_name"]
        read_file(building_name)
        # Building.objects.create(name=building_name)

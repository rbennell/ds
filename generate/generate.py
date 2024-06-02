import datetime
import random

today = datetime.date.today()


def generate(building_name: str, rows: int):
    with open(f"backend/buildings_data/{building_name}.csv", "w") as f:
        f.write("date,reading\n")
        for i in range(rows):
            day = today - datetime.timedelta(days=rows - i)
            reading = random.random() * 10
            f.write(f"{day},{reading}kWh\n")


if __name__ == "__main__":
    building_name = input("What is the name of the building?")
    rows = int(input("How many days of data would you like to generate?"))
    generate(building_name, rows)

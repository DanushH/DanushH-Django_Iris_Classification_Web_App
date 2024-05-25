import sys
import os
import django
import pandas as pd


def main():

    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_path = os.path.abspath(os.path.join(script_dir, "../"))
    sys.path.append(project_path)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "irisproject.settings")
    django.setup()

    from irisapp.models import IrisModel

    def store_data():
        csv_file_path = os.path.join(script_dir, "dataset", "Iris.csv")

        if not os.path.isfile(csv_file_path):
            return

        df = pd.read_csv(csv_file_path)

        if df.empty:
            return

        for index, row in df.iterrows():
            obj, created = IrisModel.objects.get_or_create(
                sepal_length=row["SepalLengthCm"],
                sepal_width=row["SepalWidthCm"],
                petal_length=row["PetalLengthCm"],
                petal_width=row["PetalWidthCm"],
                species=row["Species"],
            )

    store_data()


if __name__ == "__main__":
    main()

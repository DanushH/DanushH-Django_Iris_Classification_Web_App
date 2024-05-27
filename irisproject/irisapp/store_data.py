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
                sepal_length=row["sepal_length"],
                sepal_width=row["sepal_width"],
                petal_length=row["petal_length"],
                petal_width=row["petal_width"],
                species=row["species"],
            )

    store_data()


if __name__ == "__main__":
    main()

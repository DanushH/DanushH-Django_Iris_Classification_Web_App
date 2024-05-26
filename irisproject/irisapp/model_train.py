import sys
import os
import django
import pickle
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


def train_model():

    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_path = os.path.abspath(os.path.join(script_dir, "../"))
    sys.path.append(project_path)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "irisproject.settings")
    django.setup()

    from irisapp.models import IrisModel

    data = IrisModel.objects.all()
    X = []
    y = []

    for item in data:
        X.append(
            [item.sepal_length, item.sepal_width, item.petal_length, item.petal_width]
        )
        y.append(item.species)

    X = np.array(X)
    y = np.array(y)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    with open("model.pkl", "wb") as f:
        pickle.dump(model, f)


if __name__ == "__main__":
    train_model()

from django.shortcuts import render
from django.http import HttpResponse
from .models import IrisModel
import pickle
import numpy as np


with open("irisapp/model.pkl", "rb") as f:
    model = pickle.load(f)


def iris_home(request):
    return render(request, "index.html")


def iris_result(request):
    if request.method == "POST":
        sepal_length = float(request.POST.get("sepal_length"))
        sepal_width = float(request.POST.get("sepal_width"))
        petal_length = float(request.POST.get("petal_length"))
        petal_width = float(request.POST.get("petal_width"))

        input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

        prediction = model.predict(input_data)[0]
        probabilities = model.predict_proba(input_data)[0]

        context = {
            "prediction": prediction,
            "probability": probabilities,
        }
        return render(request, "result.html", context)


def iris_dataset(request):
    data = IrisModel.objects.all()
    return render(request, "dataset_table.html", {"data": data})

from django.shortcuts import render
from django.http import HttpResponse
from .models import IrisModel


def iris_home(request):
    return render(request, "index.html")


def iris_result(request):
    if request.method == "POST":
        sepal_length = request.POST.get("sepal_length")
        sepal_width = request.POST.get("sepal_width")
        petal_length = request.POST.get("petal_length")
        petal_width = request.POST.get("petal_width")

        # PREDICTION LOGIC HERE

        return render(request, "result.html")


def iris_dataset(request):
    pass
    # data = IrisModel.objects.all()
    # return render(request, "dataset_table.html", {"data": data})

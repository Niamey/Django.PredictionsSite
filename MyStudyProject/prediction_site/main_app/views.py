from django.shortcuts import render
from .models import Prediction
import random

def random_prediction(request):
    predictions = Prediction.objects.all()
    prediction = random.choice(predictions)
    return render(request, 'main_app/predictions.html', {'prediction': prediction})
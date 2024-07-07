import random
from django.core.management.base import BaseCommand
from django.utils import timezone

from main_app.models import Prediction


class Command(BaseCommand):
    help = 'Populate the database with initial predictions'

    def handle(self, *args, **kwargs):
        predictions_list = [
            "Сегодня будет успешный день",
            "Возможно, стоит задуматься о новом проекте",
            "Не забудьте про важную встречу с клиентом",
            "Поездка в отпуск станет источником вдохновения",
            "Погода будет переменчивой, не забудьте зонтик"
        ]

        for text in predictions_list:
            random_result = random.choice(['Positive', 'Negative', 'Neutral'])
            prediction = Prediction.objects.create(
                text=text,
                result=random_result,
                created_at=timezone.now()
            )
            prediction.save()

        self.stdout.write(self.style.SUCCESS('Предсказания успешно добавлены в базу данных.'))
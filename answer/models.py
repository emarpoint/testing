# from django.db import models
# from django.urls import reverse
# import datetime
# from settings import settings
# from testapp.models import Question

# class Answer(models.Model):
#     question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
#     answer = models.CharField(max_length=200, verbose_name = "Ответ")
#     votes = models.IntegerField(verbose_name = "Голосов", default = 0)
#     correct_answer = models.BooleanField(max_length=200, verbose_name = "Верный ответ")

#     class Meta:
#         verbose_name = 'Вариант ответа'
#         verbose_name_plural = 'Варианты ответа'

#     def __str__(self):
#         return self.answer
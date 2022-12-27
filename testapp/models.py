from django.db import models
from django.urls import reverse
import datetime
from settings import settings

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200,db_index=True, unique=True)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
    def __str__(self):
        return self.name
    
    
    def get_absolute_url(self):
        return reverse('testapp:product_list_by_category',
                        args=[self.slug])

class Profile(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name='products', verbose_name='Категория')
    name = models.CharField(max_length=200, verbose_name='Название теста')
    work_time = models.IntegerField(verbose_name='Время выполнения (мин)')
    questions_count = models.IntegerField(verbose_name='Количество вопросов')
    statisfactorily = models.IntegerField(verbose_name='Удовлетворительно')
    good = models.IntegerField(verbose_name='Хорошо')
    perfect = models.IntegerField(verbose_name='Отлично')
    slug = models.SlugField(max_length=200, db_index=True, null=True)

    class Meta:
        verbose_name = 'Тесты'
        verbose_name_plural = 'Тесты'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('testapp:test_detail', args=[self.id, self.slug])




class Question(models.Model):
    """Вопрос"""
    profile_name = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE, verbose_name='Название теста')
    question = models.CharField(max_length=200, verbose_name = "Вопрос")
    option1 = models.CharField(max_length=200, verbose_name = "Вариант №1")
    option2 = models.CharField(max_length=200, verbose_name = "Вариант №2")
    option3 = models.CharField(max_length=200, verbose_name = "Вариант №3")
    option4 = models.CharField(max_length=200, verbose_name = "Вариант №4")
    answer = models.CharField(max_length=200,null=True, verbose_name = "Верный ответ")
    weight = models.FloatField(default=1, verbose_name='Вес')
    date_published = models.DateTimeField(verbose_name = "Дата публикации", default = datetime.datetime.now())
    is_active = models.BooleanField(verbose_name = "Опубликован")
    slug = models.SlugField(max_length=200, db_index=True, null=True)


    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
   
    
    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return reverse('testapp:test_start', args=[ self.id])

class Result(models.Model):
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Тест')
    username = models.CharField(max_length=300, verbose_name="ФИО")
    date_time = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Время завершения")
    rating =models.FloatField(verbose_name="Проценты")

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'

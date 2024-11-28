# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

# Модель для таблиці user
class User(models.Model):
    name_user = models.CharField(max_length=30)
    email = models.EmailField(max_length=30, unique=True)
    phone_number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name_user

# Модель для таблиці courses
class Courses(models.Model):
    name_courses = models.CharField(max_length=45, unique=True)
    theme = models.CharField(max_length=45)
    type = models.CharField(max_length=45)
    price = models.IntegerField(null=True)
    level = models.CharField(max_length=45)
    duration = models.CharField(max_length=15)

    def __str__(self):
        return self.name_courses

# Модель для таблиці progress
class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    progress = models.IntegerField()

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(progress__lte=100), name="check_progress")
        ]

# Модель для таблиці payments
class Payments(models.Model):
    sum = models.IntegerField()
    date_payments = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)

# Модель для таблиці Certificate
class Certificate(models.Model):
    certificate = models.CharField(max_length=10, primary_key=True)
    date_receiving = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)

# Модель для таблиці message
class Message(models.Model):
    title_message = models.CharField(max_length=50, null=True)
    content = models.CharField(max_length=200)
    date = models.DateTimeField()

    def __str__(self):
        return self.title_message or 'Untitled'

# Модель для таблиці user_has_message
class UserHasMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['user', 'message']


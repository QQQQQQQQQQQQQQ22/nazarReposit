from django.contrib import admin
from .models import User, Courses, Progress, Payments, Certificate, Message, UserHasMessage

# Реєстрація моделей у адмінці
admin.site.register(User)
admin.site.register(Courses)
admin.site.register(Progress)
admin.site.register(Payments)
admin.site.register(Certificate)
admin.site.register(Message)
admin.site.register(UserHasMessage)


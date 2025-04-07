from django.db import models

from datetime import time

# Create your models here.
from jalali_date import datetime2jalali, date2jalali
from django.utils import timezone
from datetime import date

class Room(models.Model):
    name = models.CharField(max_length=95)
    Floor = models.IntegerField()
    room_number = models.IntegerField()

    def __str__(self):

        return f"{self.name}: اتاق شماره {self.room_number} طبقه {self.Floor}"


class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    duration = models.IntegerField(default=1)
    hour: duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.title} on {self.date}"

    def get_create_date(self):
        return datetime2jalali(self.date).strftime('%H:%M _ %y/%m/%d')

    get_create_date.admin_order_field = 'created_date'
    date.short_description = 'تاریخ ایجاد'

    def persian_int(string):
        persianize = dict(zip("0123456789", '۰۱۲۳۴۵۶۷۸۹'))
        return ''.join(persianize[digit] if digit in persianize else digit for digit in str(string))




import datetime

from django.db import models

from django.utils import timezone
from django.contrib import admin
#Tables
import django_filters
from django.utils.translation import gettext_lazy as _

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class QuestionFilter(django_filters.FilterSet):
    class Meta:
        model = Question
        fields = ["id","question_text", "pub_date"]

class AsinsToTrack(models.Model):
    asin_id = models.AutoField(primary_key=True)
    asin = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    tracking_active = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'asins_to_track'



class StockRecords(models.Model):
    stock_record_id = models.AutoField(verbose_name=_("DBID"), primary_key=True)
    asin = models.ForeignKey(AsinsToTrack, models.DO_NOTHING, blank=True, null=True)
    asin_fk = models.CharField(verbose_name=_("ASIN"), db_column='asin', max_length=100)  # Field renamed because of name conflict.
    stock_amount = models.IntegerField(verbose_name=_("Stock Amount"))
    created_at = models.DateTimeField(verbose_name=_("Date / Time"),blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'stock_records'

class  StockRecordsFilter(django_filters.FilterSet):
    asin_fk = django_filters.AllValuesMultipleFilter(lookup_expr='icontains')
    created_at = django_filters.DateFromToRangeFilter(lookup_expr='icontains')
    class Meta:
        model = StockRecords
        fields = ['stock_record_id','asin_fk',"created_at"]


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()
    class Meta:
        _use_db = 'mongodb'
from django.contrib import admin

from .models import Choice, Question, Blog, StockRecords


# Register your models here.
class StockRecordsAdmin(admin.ModelAdmin):
    list_display = ['stock_record_id','asin','asin_fk','stock_amount','created_at']
    search_fields = ['asin_fk']
    list_per_page = 10

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

#mongodb
admin.site.register(Blog)

admin.site.register(StockRecords, StockRecordsAdmin)

admin.site.register(Question, QuestionAdmin)
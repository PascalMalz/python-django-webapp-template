import django_tables2 as tables
from .models import Question, StockRecords

class StockRecordsTable(tables.Table):
    class Meta:
        model = StockRecords
        template_name = "django_tables2/bootstrap.html"
        lookup_expr = 'icontains'
        fields = ("stock_record_id", "asin_fk", "stock_amount", "created_at")
        
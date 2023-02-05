from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Choice, Question, StockRecords, AsinsToTrack
#imports from custom apps
from django.utils.decorators import method_decorator
from smartUserManagement.decorator import unauthenticated_user, allowed_users


#Table forms
from django_tables2 import SingleTableView
from .tables import StockRecordsTable
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from .models import StockRecordsFilter


from django_serverside_datatable.views import ServerSideDatatableView

# class ItemListView(ServerSideDatatableView):
# 	queryset = models.Item.objects.all()
# 	columns = ['name', 'code', 'description']



#only for ajax table test:
import requests
from django.http import HttpResponse
from django_tables2 import RequestConfig
def simple_view(request):
    tables = StockRecordsTable(StockRecords.objects.all())
    RequestConfig(request).configure(tables)
    return HttpResponse(tables.as_html(request))

@method_decorator(allowed_users(allowd_roles=['admin']),name='dispatch')
class StockRecordsListView(SingleTableMixin, FilterView):
    table_class = StockRecordsTable
    model = StockRecords
    
    template_name = 'polls/best_seller.html'
    filterset_class = StockRecordsFilter
    
#...

#tutorial Outside Configuration tables
def table_server_side(request):
    print("start")
    stock_records_list = StockRecords.objects.all()
    print("end")
    return render(request,'polls/table_server_side.html')

class Data(ServerSideDatatableView):
    queryset = StockRecords.objects.all()
    columns = ['stock_record_id','asin','asin_fk','stock_amount','created_at']

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


@method_decorator(allowed_users(allowd_roles=['admin']),name='dispatch')
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

@method_decorator(allowed_users(allowd_roles=['admin']),name='dispatch')
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

@method_decorator(allowed_users(allowd_roles=['admin']),name='dispatch')
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


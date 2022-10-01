from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Sale
from .forms import SalesSearchForm
import pandas as pd
# Create your views here.

def home_view(request):
    form = SalesSearchForm(request.POST or None)  # "or None" will stop form from submitting automatically when page loads

    if request.method == "POST":
        sale_df = None 
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        chart_type = request.POST.get('chart_type')
        print(chart_type, date_from, date_to)

        sale_qs = Sale.objects.filter(created__date__lte=date_to, created__date__gte=date_from)
        if len(sale_qs) > 0:    
            print("######################################")
            sales_df = pd.DataFrame(sale_qs.values())
            positions_data = []
            for sale in sale_qs:
                for pos in sale.get_positions():
                    obj = {
                        'position_id' : pos.id,
                        'product' : pos.product.name,
                        'quantit' : pos.quantity,
                        "price" : pos.price,
                        'sales_id' : pos.get_sales_id()
                    }
                    positions_data.append(obj)

            sales_df = sales_df.to_html

            positions_df = pd.DataFrame(positions_data)
            positions_df = positions_df.to_html 
            print(positions_df)
            print("######################################")
        else:
            print('no data')


    context = {
        "form" : form,
        'sales_df' : sales_df,
        'positions_df' : positions_df,
    }
    
    return render(request, 'sales/home.html', context)



class SaleListView(ListView):
    model = Sale
    template_name = 'sales/main.html'

# def sale_list_view(request):
#     qs = Sale.objects.all()
#     return render(request, 'sales/main.html', {'object_list' : object})



class SaleDetailView(DetailView):
    model = Sale
    template_name = 'sales/detail.html'

# def sale_detail_view(request, pk):
#     qs = Sale.objects.get(pk = pk)
#     return render(request, 'sales/detail.html', {'object' : object})




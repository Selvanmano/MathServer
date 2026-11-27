from django.shortcuts import render

def  cumchurn_area(request):
    
    Customers_count = float(request.POST.get('Customers_count', '0'))
    Initial_Customer = float(request.POST.get('Initial_Customer', '0'))
    area =( ( Initial_Customer - Customers_count ) / Initial_Customer ) * 100 if request.method == 'POST' and Initial_Customer else 0

    print("Customers lost count =", Customers_count)
    print("Initial customers count =", Initial_Customer)
    print("Churn Rate =", area)

    return render(
        request,
        'sgapp/sam.html',
        {'Customers_count': Customers_count, 'Initial_Customer': Initial_Customer, 'area': area}
    )


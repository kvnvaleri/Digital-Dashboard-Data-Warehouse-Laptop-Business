from django.shortcuts import render
from .models import DimLaptop, FactHarga

def dashboard(request):
    # Ambil data laptop dan harga
    laptops = DimLaptop.objects.all()
    avg_prices = FactHarga.objects.values('laptopid__company').annotate(avg_price=models.Avg('price_euros'))

    context = {
        'laptops': laptops,
        'avg_prices': avg_prices,
    }
    return render(request, 'dashboard/dashboard.html', context)
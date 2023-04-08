from django.shortcuts import render


from .models import Bolimlar, Hodim_haqida, Hodimlar, Qarindoshlik


# List View metodi orqali backenddagi malumotlarni frontendga o'tqazish va belgilab olish uchun yoziladi

from django.views.generic import ListView
class HodimlarView(ListView):
    model = Hodimlar
    template_name = "index.html"
    context_object_name = "Hodim"


# views - Ko'rish. Foydalanuvchi ko'rib ishlatib boradigan qism - views.py

# def index(request):
#     bolim = Bolimlar.objects.all()
#     contex = {
#         'bolim':bolim
#     }
#     return render(request, 'index.html', contex)



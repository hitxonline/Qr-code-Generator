from django.shortcuts import render
from .models import Codes
import Qr_code_generator.generator as generator

# Create your views here.


def home(request):
    
    if request.method == 'POST':
        link = request.POST.get('link')
        link_from = request.POST.get('link_from')
        holder_status = request.POST.get('holder_status')

        link_from = str(link_from)
        link_from = link_from.upper()

        qr_code = Codes.objects.create(link=link, link_from=link_from, holder_status=holder_status)
        qr_code.save()

        Id = qr_code.id

        generator.Code_generating(qr_code.link, Id)
        generator.merging(Id)
        generator.Texting(Id, holder_status, link_from)

        image = '/image'+str(Id)+'.jpg'
        qr_code = Codes.objects.filter(id=Id).update(image=image)

        final_result = Codes.objects.filter(id=Id)

        return render(request, 'index.html', {'qr_code':final_result})
        
    return render(request, 'index.html')
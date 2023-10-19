from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import table

from django.http import JsonResponse
# Create your views here.

def search_page(request):
    return render(request, 'search_page.html')

def chat(request):
    element_id = request.GET.get('id')
    entry = table.objects.filter(ids=element_id).order_by('ids').first()
        
    return render(request, 'chat.html', {'entry': entry})


def home(request):
    return render(request, 'base.html')

from django.db.models import Q

def get_names(request):
    search = request.GET.get('search')
    payload = []

    if search:
        # QuerySet for names starting with search term
        starts_with_qs = table.objects.filter(title__istartswith=search)
        
        # QuerySet for names containing search term but not starting with it
        contains_qs = table.objects.filter(Q(title__icontains=search) & ~Q(title__istartswith=search))
        
        # Combining both QuerySets
        objs = list(starts_with_qs) + list(contains_qs)

        for obj in objs:
            payload.append({
                'ids': obj.ids,
                'query': obj.query,
                'title': obj.title,
                'dose': obj.strength,
                'labeler': obj.labeler
            })

    return JsonResponse({
        'status': True,
        'payload': payload
    })

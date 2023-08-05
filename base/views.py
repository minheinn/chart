from django.shortcuts import render
from . models import Profile

# Create your views here.
def index(request):
    labels = []
    data = []
    queryset = Profile.objects.order_by('-age')[:5]
    for person in queryset:
        labels.append(person.name)
        data.append(person.age)
        

    return render(request, 'pages/index.html', {'labels':labels, 'data':data})
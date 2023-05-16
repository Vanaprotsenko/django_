from django.shortcuts import render



def main(request):
    return render(request, 'app/index.html')

def info(request,name,surname,old,city,job):
    context = {
        'name':name,
        'surname':surname,
        'old':old,
        'city':city,
        'job':job
    }
    return render(request, 'app/anketa.html',context)

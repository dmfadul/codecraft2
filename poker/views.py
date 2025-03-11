from django.shortcuts import render

def range(request):
    return render(request=request, template_name='poker/range.html')

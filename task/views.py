from django.http import JsonResponse
from django.shortcuts import render
from .forms import NumberForm
from .utils import get_the_number
from .models import Number

def index(request):
    form = NumberForm()
    return render(request, 'base.html', {'form': form})


def post_form(request):
    form = NumberForm(request.POST)
    if form.is_valid():
        get_number = form.cleaned_data.get("get_number")
        if get_number <= 92233720368:
            number, create = Number.objects.get_or_create(get_number=get_number)
            if create:
                fibonancci_number = get_the_number(get_number)
                number.fibonacci_number = fibonancci_number
                number.save()
            else:
                fibonancci_number = number.fibonacci_number
            fibonancci_number = 'Nearest fibonacci number: ' + str(fibonancci_number)
        else:
            fibonancci_number = 'too many'
    else:
        fibonancci_number = 'Error'
    return JsonResponse({"fibonancci_number": fibonancci_number})
    # return render(request, 'base.html', context)

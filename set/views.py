from django.shortcuts import render

def book_list(request):
    return render(request, 'set/book_list.html', {})

def company_list(request):
    return render(request, 'set/company_list.html', {})

from django.shortcuts import render
from .models import Drug
# Create your views here.
def databasePage(request):
    if request.method == "POST":
        query = request.POST.get('query')
        message = "false"
        searchItem = request.POST.get('search-item')
        if query == 'drugbankId':
            try:
                drugbankId = Drug.objects.get(drugbankId=searchItem)
            except Drug.DoesNotExist:
                drugbankId = None
                message = "true"
        elif query == 'drugName':
            try:
                drugbankId = Drug.objects.get(drugName=searchItem)
            except Drug.DoesNotExist:
                drugbankId = None
                message = "true"
        else:
            try:
                drugbankId = Drug.objects.get(geneSymbol=searchItem)
            except Drug.DoesNotExist:
                drugbankId = None
                message = "true"
        print(drugbankId)
        context = {'data': drugbankId, 'message': message}
        return render(request, 'databasePage.html', context)

    context = {'message': "false"}
    return render(request, 'databasePage.html', context)
from django.shortcuts import HttpResponse, loader, render

# Create your views here.

def testpage(request):
    template=loader.get_template('test.html')
    return HttpResponse(template.render())
# loads test page

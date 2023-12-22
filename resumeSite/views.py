from django.shortcuts import render

# Create your views here.
def page_not_found_view(request, exception):
    return render(request, 'resumeSite/404.html', status=404)


def resume(request):
    return render(request,'resumeSite/resume.html')
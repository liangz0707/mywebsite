from django.http import HttpResponse

def index(request):
    print "aaa"
    return HttpResponse("Hello, world. You're at LiangZhe's Site")


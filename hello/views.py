from django.http import HttpResponse



def cookie(request):
    print(request.COOKIES)
    old_value = request.COOKIES.get('count', 1)
    resp = HttpResponse('fc879743 view count='+str(old_value))
    if old_value:
        resp.set_cookie('count', int(old_value)+1)
    else:
        resp.set_cookie('count', 1)
    resp.set_cookie('dj4e_cookie', 'fc879743', max_age=1000)


    return resp
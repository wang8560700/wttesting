from django.http import JsonResponse
from sign.models import Event
from sign.models import Guest
from django.core.exceptions import *
from django.db.utils import IntegrityError
import time
from django.http import HttpResponse,HttpResponseRedirect

def add_event(request):
    if request.method=="POST":
        eid=request.POST.get("eid",'')
        name=request.POST.get("name",'')
        limit=request.POST.get("limit",'')
        status=request.POST.get("status",'')
        address=request.POST.get("address",'')
        start_time=request.POST.get("start_time",'')
        if eid=="" or name=="" or limit=="" or address=="" or start_time=="":
            return JsonResponse({"status":10021,"message":"necessary reparameter is null!"})
        try:
            int(eid)
        except ValueError:
            return JsonResponse({"status":10025,"message":"eid formate erro!"})
        try:
            int(limit)
        except ValueError:
            return JsonResponse({"status":10026,"message":"limit formate erro!"})
        result=Event.objects.filter(id=eid)
        if result:
            return JsonResponse({"status":10022,"message":"eid is already exist!"})
        result=Event.objects.filter(name=name)
        if result:
            return JsonResponse({"status":10023,"message":"name is already exist!"})
        if status=="":
            status=1
        try:
            Event.objects.create(id=eid,name=name,limit=limit,address=address,status=int(status),start_time=start_time)
            return JsonResponse({'status':200,'message':'add event success!'})
        except ValidationError:
            return JsonResponse({"status":10024,"message":"date format erro! reference: YYYY-MM-DD HH:MM:SS"})

    else:
        return JsonResponse({"status":10031,"message":"request method erro!"})
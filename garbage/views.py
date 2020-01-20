from django.shortcuts import render,HttpResponse
from garbage.models import garbage_report,potholes_report,cattles_report
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    garbage = garbage_report.objects.all()
    potholes = potholes_report.objects.all()
    cattles = cattles_report.objects.all()
    dict = {'garbage':garbage, 'potholes':potholes, 'cattles':cattles}
    return render(request,'index.html',dict)

def complete1(request):
    image = request.POST["submit1"]
    garbage_sub = garbage_report.objects.get(image_url=image)
    garbage_sub.status = True
    garbage_sub.save()
    

    garbage = garbage_report.objects.all()
    potholes = potholes_report.objects.all()
    cattles = cattles_report.objects.all()
    dict = {'garbage':garbage, 'potholes':potholes, 'cattles':cattles}
    return render(request,'index.html',dict)

def complete2(request):
    image = request.POST["submit2"]
    pothole_sub = potholes_report.objects.get(image_url=image)
    pothole_sub.status = True
    pothole_sub.save()
    

    garbage = garbage_report.objects.all()
    potholes = potholes_report.objects.all()
    cattles = cattles_report.objects.all()
    dict = {'garbage':garbage, 'potholes':potholes, 'cattles':cattles}
    return render(request,'index.html',dict)

def complete3(request):
    image = request.POST["submit3"]
    cattle_sub = cattles_report.objects.get(image_url=image)
    cattle_sub.status = True
    cattle_sub.save()
    

    garbage = garbage_report.objects.all()
    potholes = potholes_report.objects.all()
    cattles = cattles_report.objects.all()
    dict = {'garbage':garbage, 'potholes':potholes, 'cattles':cattles}
    return render(request,'index.html',dict)

@csrf_exempt
def post(request,id,image,imgloc,tag):
    img = "http://akshatkhanna.co/upload/"+ image
    if(tag==0):
        garbage_report.objects.create(user_id=id, image_url=img, location=imgloc)
    if(tag==1):
        potholes_report.objects.create(user_id=id, image_url=img, location=imgloc)
    if(tag==2):
        cattles_report.objects.create(user_id=id, image_url=img, location=imgloc)
    return HttpResponse("Successfully registered!!")
from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from streamapp.camera import VideoCamera, IPWebCam, LiveWebCam
from .models import Cam_Configer,Empolys,Know,Unknow,CameraName,Cam_con
import datetime
from django.utils import timezone
from .forms import Show,ShowDate,ShowTime,Showun,Showund
# Create your views here.


def index(request):
	cname=CameraName.objects.all()
	now = datetime.datetime.now()
	var={
		"cname":cname,
		"time":now,
	}
	return render(request,'streamapp/home.html',var)
def show(request,id):
	pk=Know.objects.get(pk=id)
	show=Show(instance=pk)
	showtime=ShowTime(instance=pk)
	showdate=ShowDate(instance=pk)
	prim='http://127.0.0.1:8000/static/stor/develop-a-professional-python-django-websites.jpg'
	var={
		'show':show,
		'showtime':showtime,
		'showdate':showdate,
		'prim':prim,
	}
	return render(request,"streamapp/show.html",var)
def showun(request,id):
	pk=Unknow.objects.get(pk=id)
	showtime=Showun(instance=pk)
	showdate=Showund(instance=pk)
	var={
		'showtime':showtime,
		'showdate':showdate

	}
	return render(request,"streamapp/show.html",var)

def report(request):
	if request.method=="POST":
		select1=request.POST.get("selector_known_or_gust")
		select2=request.POST.get("selector_entry_exit")
		if select1=="known":
			status=Know.objects.all()
			VAR={
    		"status":status,
    		}
			return render(request,"streamapp/configuration.html",VAR)

		elif select1=="gust":
			status=Unknow.objects.all()
			VAR={
    		"status1":status,
    		}
			return render(request,"streamapp/configuration.html",VAR)
		tfrom=request.POST.get("from")
		t_to=request.POST.get("to")
	return render(request,"streamapp/configuration.html")
def configuration(request):
	if request.method=="POST":
		names=request.POST.get("name")
		password=request.POST.get("password")
		ipaddrss=request.POST.get("ipaddress")
		cameraname=request.POST.get("cname")
		fm=Cam_Configer(name=names,pasw=password,ip_address=ipaddrss,camera_number=cameraname)
		fm.save()
		return render(request,"streamapp/report.html",{"success":"Report Update successfully"})
	return render(request,"streamapp/report.html")
def configuration2(request):
	if request.method=="POST":
		names=request.POST.get("name")
		password=request.POST.get("password")
		ipaddrss=request.POST.get("ipaddress")
		cameraname=request.POST.get("cname")
		fm=Cam_con(Name=names,Password=password,Ip_address=ipaddrss,Camera_NO=cameraname)
		fm.save()
		return render(request,"streamapp/camera2.html",{"success":"Report Update successfully"})
	return render(request,"streamapp/camera2.html")
def addemp(request):
	if request.method=="POST":
		e_id=request.POST.get("id")
		name=request.POST.get("name")
		mobile=request.POST.get("mobile")
		pic=request.FILES["img"]
		try:
			user=Empolys.objects.get(ids=e_id)
			return render(request,"streamapp/addemp.html",{'error':"User ID already exists"})
		except Empolys.DoesNotExist:
			efm=Empolys(ids=e_id,name=name,mobile_no=mobile,image=pic)
			efm.save()
			return render(request,"streamapp/addemp.html",{"sucess":"your information is uploaded successfully"})
	return render(request,"streamapp/addemp.html")
def emplist(request):
	emplist=Empolys.objects.all()
	htmlvar={
		'emplist':emplist
	}
	return render(request,"streamapp/emplist.html",htmlvar)



def viewemp(request,id):
	ids=id
	name=Empolys.objects.filter(ids=ids)
	return render(request,"streamapp/viewemp.html",{'name':name})

def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def video_feed(request):
	return StreamingHttpResponse(gen(VideoCamera()),
					content_type='multipart/x-mixed-replace; boundary=frame')


def webcam_feed(request):
	return StreamingHttpResponse(gen(IPWebCam()),
					content_type='multipart/x-mixed-replace; boundary=frame')


'''def mask_feed(request):
	return StreamingHttpResponse(gen(MaskDetect()),
					content_type='multipart/x-mixed-replace; boundary=frame')'''
					
def livecam_feed(request):
	return StreamingHttpResponse(gen(LiveWebCam()),
					content_type='multipart/x-mixed-replace; boundary=frame')

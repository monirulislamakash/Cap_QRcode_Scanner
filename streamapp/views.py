from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from streamapp.camera import VideoCamera
from .models import Cam_Configer,Empolys,Know,Unknow,CameraName,Cam_con
import datetime
import requests
from django.utils import timezone
from .forms import Show,ShowDate,ShowTime,Showun,Showund
# Create your views here.


def index(request):
	mainurl=''
	if request.method=="POST":
		url=request.POST.get('url')
		mainurl=mainurl+url
		print(mainurl)
		r = requests.get(mainurl)
		with open('1.jpg', 'wb') as f:
			f.write(r.content)
			return render(request,'streamapp/home.html')
	return render(request,'streamapp/home.html')


def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def video_feed(request):
	return StreamingHttpResponse(gen(VideoCamera()),
					content_type='multipart/x-mixed-replace; boundary=frame')

'''def mask_feed(request):
	return StreamingHttpResponse(gen(MaskDetect()),
					content_type='multipart/x-mixed-replace; boundary=frame')'''
					
def livecam_feed(request):
	return StreamingHttpResponse(gen(LiveWebCam()),
					content_type='multipart/x-mixed-replace; boundary=frame')

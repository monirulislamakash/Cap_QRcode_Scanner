from django.contrib import admin
from .models import Cam_Configer,Empolys,Know,Unknow,CameraName,Cam_con
# Register your models here.
admin.site.register(Cam_Configer)
admin.site.register(CameraName)
admin.site.register(Empolys)
admin.site.register(Know)
admin.site.register(Unknow)
admin.site.register(Cam_con)
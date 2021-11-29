from django import forms
from .models import Know,Cam_Configer,Cam_con
class Show(forms.ModelForm):
     class Meta:
        model=Know
        fields=["ids"]
        widgets={
            "ids":forms.TextInput(attrs={"style":"border:0px;"}),
        }
class ShowDate(forms.ModelForm):
     class Meta:
        model=Know
        fields=["data"]
        widgets={
            "data":forms.TextInput(attrs={"style":"border:0px;"}),
        }
class ShowTime(forms.ModelForm):
     class Meta:
        model=Know
        fields=["time"]
        widgets={
            "time":forms.TextInput(attrs={"style":"border:0px;"}),
        }
class Showun(forms.ModelForm):
    class Meta:
        model=Know
        fields=["time"]
        widgets={
            "time":forms.TextInput(attrs={"style":"border:0px;"}),
        }
class Showund(forms.ModelForm):
    class Meta:
        model=Know
        fields=["data"]
        widgets={
            "data":forms.TextInput(attrs={"style":"border:0px;"}),
        }


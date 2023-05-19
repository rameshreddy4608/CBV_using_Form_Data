from typing import Any, Dict
from django.shortcuts import render
from app.forms import *
# Create your views here.
from django.views.generic import TemplateView
from django.http import HttpResponse
class CBV_using_Form_Data(TemplateView):
    template_name='CBV_using_Form_Data.html'


    def get_context_data(self, **kwargs):
        ECO=super().get_context_data(**kwargs)
        ECO['SFO']=StudentForm()
        return ECO
    
    def post(self,request):
        SFO=StudentForm(request.POST)
        if SFO.is_valid():
            SFO.save()
            return HttpResponse('data inserted sucessfully')
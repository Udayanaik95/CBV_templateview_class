from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class cbv_context(TemplateView):
    template_name='cbv_context.html'

    def get_context_data(self, **kwargs):
        EDCO=super().get_context_data(**kwargs)
        EDCO['name']="UDAYA"
        EDCO['age']=25
        return EDCO
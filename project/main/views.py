from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render
from main.models import Users
from django.views.generic import ListView,TemplateView


class AllUsersView(ListView):
    model = Users
    template_name = 'all.html'
    context_object_name = 'all'
    
    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset()

class UserInformation(TemplateView):
    template_name = 'user.html'
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['user_id'] = Users.objects.filter(pk = self.kwargs['user_id']).first()
        
        return context
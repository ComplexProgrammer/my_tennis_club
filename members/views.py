from unittest import loader
from django.shortcuts import render, get_object_or_404
from .models import Member
from django.views.generic import ListView, DetailView
# def members(request):
#     members=Member.objects.all()
#     context={
#         "members":members
#     }
#     return render(request, 'members.html', context=context)

# def member_detail_view(request, id):
#     member = get_object_or_404(Member, id=id)
#     context={
#         "member": member
#     }
#     return render(request, "member_detail.html", context=context)
class members(ListView):
    model=Member
    template_name="members.html"
    context_object_name="members"
class member_detail_view(DetailView):
    model=Member
    template_name="member_detail.html"
    context_object_name="member"

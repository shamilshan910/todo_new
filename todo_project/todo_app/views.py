from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import task_holder
from .forms import todo_form
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
# Create your views here.

class generic_list(ListView):
    model=task_holder
    template_name = 'home.html'
    context_object_name = 'key'
class generic_detial(DetailView):
    model = task_holder
    template_name = 'detial_class.html'
    context_object_name = 'data'

# class generic_update(UpdateView):
#     model = task_holder
#     fields = ('name','priority','date')
#     template_name = 'updated.html'
#     context_object_name = 'form'
#     def get_success_url(self):
#         return reverse_lazy('/',kwargs={'pk':self.object.id})

def index(request):
    datas = task_holder.objects.all()
    if request.method=='POST':
        date1=request.POST.get('get_date','')
        name1=request.POST.get('get_task','')
        priority1=request.POST.get('get_priority','')
        task=task_holder(name=name1,priority=priority1,date=date1)
        task.save()

    return render(request,"index.html",{'data':datas})
def cancel(request):
    return render(request,'index.html')

# def detials1(request):
#
#     return render(request,'detials.html',)
def delete(request,task_id):
    task=task_holder.objects.get(id=task_id)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'dele.html')

def update(request,f_id):
    model=task_holder.objects.get(id=f_id)
    form=todo_form(request.POST or None,instance=model)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'task':model})
def cancel1(request):
    datas=task_holder.objects.all()
    return redirect('/',{'data':datas})
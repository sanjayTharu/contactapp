from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import DetailView,DeleteView,UpdateView,ListView,CreateView
from .models import Contact
from .forms import ContactUploadForm

# Create your views here.

class ContactCreateView(CreateView):
    model= Contact
    success_url= "/"
    template_name='contacts/contact_create.html'
    fields=["first_name","last_name","surname","phone","email"]

class ContactListView(ListView):
    model = Contact
    template_name='contacts/contact_list.html'

def search(request):
    if request.method=="POST":
        query=request.POST.get('surname',None)
        if query:
            results=Contact.objects.filter(title__contains=query)
            return render(request,'contacts/search.html',{'contacts':results})
        
    return render(request,'contacts/search.html')


def contact_update(request,pk):
    obj=get_object_or_404(Contact,pk=pk)
    form=ContactUploadForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    context={
        'form':form
    }
    return render(request,'contacts/contact_update.html',context)

class ContactDeleteView(DeleteView):
    template_name="contacts/contact_delete.html"
    success_url='/'
    model= Contact

class ContactDetailView(DetailView):
    template_name="contacts/contact_detail.html"
    model= Contact



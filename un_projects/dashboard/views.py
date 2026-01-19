from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Staff_Member
from .forms import StaffMemberForm

@login_required(login_url='/accounts/login/')
def home(request):
    get_all_staff =Staff_Member.objects.all()
    context = {'employees': get_all_staff}
    return render(request, 'un_portal/home.html', context)

@login_required(login_url='/accounts/login/')
def create_staff_member(request):
    if request.method == 'POST':
        form = StaffMemberForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('home')
    else:
        form = StaffMemberForm() 
    context ={
		'title': 'add employee',
		'form': form,
	}
    return render(request, 'un_portal/form.html', context)




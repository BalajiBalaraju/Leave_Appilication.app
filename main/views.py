from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import LeaveApplication
from .forms import LeaveApplicationForm

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('leave_list')
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def leave_list(request):
    # Students see only their own applications
    leaves = LeaveApplication.objects.filter(student=request.user).order_by('-applied_on')
    return render(request, 'main/leave_list.html', {'leaves': leaves})

@login_required
def leave_create(request):
    if request.method == "POST":
        form = LeaveApplicationForm(request.POST)
        if form.is_valid():
            leave = form.save(commit=False)
            leave.student = request.user
            leave.save()
            return redirect('leave_list')
    else:
        form = LeaveApplicationForm()
    return render(request, 'main/leave_form.html', {'form': form})

@login_required
def leave_update(request, pk):
    leave = get_object_or_404(LeaveApplication, pk=pk, student=request.user)
    if request.method == "POST":
        form = LeaveApplicationForm(request.POST, instance=leave)
        if form.is_valid():
            form.save()
            return redirect('leave_list')
    else:
        form = LeaveApplicationForm(instance=leave)
    return render(request, 'main/leave_form.html', {'form': form})

@login_required
def leave_delete(request, pk):
    leave = get_object_or_404(LeaveApplication, pk=pk, student=request.user)
    if request.method == "POST":
        leave.delete()
        return redirect('leave_list')
    return render(request, 'main/leave_confirm_delete.html', {'leave': leave})

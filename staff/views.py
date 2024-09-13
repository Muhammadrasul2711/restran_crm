from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_requierd
from Crmapp.models import Staff



def staff_list(request):
    staffs = Staff.objects.all()
    return render(request, 'staff/staff_list.html', {'staffs': staffs})




def staff_create(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        position_id = request.POST.get('position_id')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        is_active = request.POST.get('is_active') == 'on'


        Staff.objects.create(
            full_name=full_name,
            position_id=position_id,
            email=email,
            phone=phone,
            is_active=is_active
        )
        return redirect('staff_list')

    return render(request, 'staff/staff_form.html')


def staff_update(request, id):
    staff = get_object_or_404(Staff, id=id)
    if request.method == "POST":
        staff.full_name = request.POST.get('full_name')
        staff.position_id = request.POST.get('position_id')
        staff.email = request.POST.get('email')
        staff.phone = request.POST.get('phone')
        staff.is_active = request.POST.get('is_active') == 'on'
        staff.save()
        return redirect('staff_list')

    return render(request, 'staff/staff_form.html', {'staff': staff})



def staff_delete(request, id):
    staff = get_object_or_404(Staff, id=id)
    if request.method == "POST":
        staff.delete()
        return redirect('staff_list')
    return render(request, 'staff/staff_confirm_delete.html', {'staff': staff})

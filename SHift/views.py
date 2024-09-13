from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_requierd
from Crmapp.models import SHift
from django.http import HttpResponse



def shift_list(request):
    shifts = SHift.objects.all()
    return render(request, 'shift/shift_list.html', {'shifts': shifts})



def shift_create(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')


        SHift.objects.create(
            full_name=full_name,
            start_time=start_time,
            end_time=end_time
        )
        return redirect('shift_list')

    return render(request, 'shift/shift_form.html')




def shift_update(request, id):
    shift = get_object_or_404(SHift, id=id)
    if request.method == "POST":
        shift.full_name = request.POST.get('full_name')
        shift.start_time = request.POST.get('start_time')
        shift.end_time = request.POST.get('end_time')
        shift.save()
        return redirect('shift_list')

    return render(request, 'shift/shift_update.html', {'shift': shift})




def shift_delete(request, id):
    shift = get_object_or_404(SHift, id=id)
    if request.method == "POST":
        shift.delete()
        return redirect('shift_list')
    return render(request, 'shift/shift_confirm_delete.html', {'shift': shift})


def shift_detail(request, id):
    shift = get_object_or_404(SHift, id=id)
    return render(request, 'shift/shift_detail.html', {'shift': shift})

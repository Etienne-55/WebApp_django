from django.shortcuts import render, get_list_or_404, redirect
from .models import computer_hardware
from .forms import computer_hardware_form
from django.shortcuts import get_object_or_404

def inventory_list(request):
    inventory = computer_hardware.objects.all()
    return render(request, 'stock_app/inventory_list.html', {'inventory': inventory, 'view': 'list'})

def inventory_detail(request, pk):
    inventory = get_object_or_404(computer_hardware, pk=pk)
    return render(request, 'stock_app/inventory_list.html', {'inventory': inventory, 'view': 'detail'})

def add_inventory(request):
    if request.method == "POST":
        form = computer_hardware_form(request.POST)
        if form.is_valid():
            inventory = form.save()
            return redirect('inventory_detail', pk=inventory.pk)
    else:
        form = computer_hardware_form()
    return render(request, 'stock_app/inventory_list.html', {'form': form, 'view': 'form'})

from django.shortcuts import get_object_or_404

def edit_inventory(request, pk):
    inventory = get_object_or_404(computer_hardware, pk=pk)
    if request.method == "POST":
        form = computer_hardware_form(request.POST, instance=inventory)
        if form.is_valid():
            inventory = form.save()
            return redirect('inventory_detail', pk=inventory.pk)
    else:
        form = computer_hardware_form(instance=inventory)
    return render(request, 'stock_app/inventory_list.html', {'form': form, 'view': 'form'})


def delete_inventory(request, pk):
    inventory = get_object_or_404(computer_hardware, pk=pk)
    if request.method == "POST":
        inventory.delete()
        return redirect('inventory_list')
    return render(request, 'stock_app/inventory_list.html', {'inventory': inventory, 'view': 'delete'})

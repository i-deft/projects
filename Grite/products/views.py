from django.shortcuts import render
from .models import Division, Reagent, ReagentsFile


def divisions(request):
    divisions_names = Division.objects.all()
    context = {'divisions_names': divisions_names}
    return render(request, 'products/divisions.html', context)


def division(request, division_slug):
    division_name = Division.objects.get(slug=division_slug)
    reagents_names = division_name.reagent_set.all()
    context = {'division_name': division_name, 'reagents_names': reagents_names}
    return render(request, 'products/division.html', context)


def reagent(request, division_slug, reagent_slug):
    reagent_name = Reagent.objects.get(slug=reagent_slug)
    reagent_files = reagent_name.reagentsfile_set.all()
    context = {'reagent_files': reagent_files, 'reagent_name': reagent_name}
    return render(request, 'products/reagent.html', context)



from .models import Division


def add_variable_to_context(request):
    divisions = Division.objects.all()
    return {
        'divisions': divisions
    }
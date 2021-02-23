from .models import Contacts


def add_variable_to_context(request):
    contact_info = Contacts.objects.all().latest('id')
    return {
        'contact_info': contact_info,
    }

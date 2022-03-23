from django.shortcuts import redirect


def main_view(request):
    response = redirect('api/')
    return response

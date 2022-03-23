from django.shortcuts import redirect


def index_view(request):
    response = redirect('sewpatd:api-root')
    return response

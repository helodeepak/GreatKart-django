from .models import Subject_Category

def menu_link(request):
    links=Subject_Category.objects.all()
    return dict(links=links)
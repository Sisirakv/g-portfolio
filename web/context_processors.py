from .models import Category

def main_context(request):
    category = Category.objects.all()
    return {
        'category':category,
        'domain':request.META['HTTP_HOST']
    }
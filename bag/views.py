from django.shortcuts import render

# Create your views here.
def view_bag(request):
    """A view that ernders the bag contents screen"""
    
    return render(request, 'bag/bag.html')
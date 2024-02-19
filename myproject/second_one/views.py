""" this is data take in database"""

# from django.shortcuts import render,redirect
# from .models import Products

""" this is the first page view """

"""def firstpage(request):
    if request.user.is_authenticated:
        dict_pdt = {
            'values': Products.objects.all()
        }
        return render(request, 'firstpage.html', dict_pdt)
    return redirect('signup') """



""" this is data take in cache"""




from django.shortcuts import render, redirect
from django.core.cache import cache
from .models import Products

# Cache timeout
CACHE_TIMEOUT = 120

def firstpage(request):
    if request.user.is_authenticated:

        # Retrieve the  count cookie
        visit_count = request.COOKIES.get('visit_count', '0')
        visit_count = int(visit_count) + 1

        # Retrieve product listing 
        product_listing = cache.get('product_listing')

        # If not in cache, add the values
        if not product_listing:
            product_listing = Products.objects.all()
            # Set the cache
            cache.set('product_listing', product_listing, timeout=CACHE_TIMEOUT)

        # Create an HttpResponse object
        response = render(request, 'firstpage.html', {'values': product_listing, 'visit_count': visit_count})

        # Add the visit count cookie to the response
        response.set_cookie('visit_count', visit_count)

        # Return the response
        return response
    
    # If not authenticated, redirect to the signup page
    return redirect('signup')

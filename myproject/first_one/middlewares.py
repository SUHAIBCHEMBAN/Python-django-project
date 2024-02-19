from django.shortcuts import redirect

class Customadminpanel:

    """ middleware to redirect non-superuser authenticated users from the admin panel """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        """ Check if the request is for the admin panel and the user is a regular user """

        if request.path.startswith('/admin/') and not request.user.is_superuser and request.user.is_authenticated:
            return redirect('/firstpage/') 
        
        response = self.get_response(request)
        return response

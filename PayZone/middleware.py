import logging
from django.contrib.auth import logout

logger = logging.getLogger(__name__)

class SessionTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            # Log the session age for debugging
            logger.debug(f'Session age: {request.session.get_expiry_age()}')

            if request.session.get_expiry_age() <= 0:
                logout(request)

        response = self.get_response(request)
        return response

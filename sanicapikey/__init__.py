from functools import wraps
from sanic import Sanic, exceptions

class SanicApiKey:
    def __init__(self, app=None,
                arg='key',
                header=None,
                form=None,
                keys=None,
                error='Auth required.'
                ):
        self.api_keys = keys
        self.header = header
        self.arg = arg
        self.form = form
        self.error = error

        if app is not None:
            self.init_app(app)

    def init_app(self, app: Sanic):
        """hook on request start etc."""
        app.register_middleware(self.open_session, 'request')

    async def open_session(self, request):
        pass

    async def _is_api_key(self, request):
        """
        check key is valid api key
        """

        if self.header:
            token = request.headers.get(self.header, None)
        elif self.form:
            if self.form in request.form:
                token = request.form[self.form][0]
            else:
                token = None
        else:
            if self.arg in request.args:
                token = request.args[self.arg][0]
            else:
                token = None

        self.token = token
        return token in self.api_keys

    def get_token(self):
        """
        Get logged api key
        """

        return self.token if self.token else ''
    
    def add_key(self, key : str):
        """
        Add API Key.
        """

        self.api_keys.append(key)

    def key_required(self, handler=None):
        """
        wrapper
        """
        
        @wraps(handler)
        async def wrapper(request, *args, **kwargs):
            if not await self._is_api_key(request):
                if hasattr(self.error, '__call__'):
                    return await self.error(request)
                else:
                    raise exceptions.Unauthorized(self.error)
            return await handler(request, *args, **kwargs)
        return wrapper

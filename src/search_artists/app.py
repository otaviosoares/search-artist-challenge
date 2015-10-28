from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response


def search(request):
    url = request.url
    mixAge = int(request.params.get('min', 0))
    maxAge = int(request.params.get('max', 100))

    body = 'URL %s with name: %d' % (url, maxAge)
    return Response(
        content_type="text/json",
        body=body
    )


if __name__ == '__main__':
    config = Configurator()
    config.add_route('search', '/')
    config.add_view(search, route_name='search')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    print 'Server running at %s' % 'http://localhost:6543/'
    server.serve_forever()

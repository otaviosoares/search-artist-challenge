from wsgiref.simple_server import make_server
from pyramid.config import Configurator

from search_artists.views import search

if __name__ == '__main__':
    config = Configurator()
    config.include('pyramid_chameleon')
    config.add_route('search', '/')
    config.add_view(search, route_name='search')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    print 'Server running at %s' % 'http://localhost:6543/'
    server.serve_forever()

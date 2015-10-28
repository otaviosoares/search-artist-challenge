from pyramid.view import view_config
from searcher import ArtistSearcher


@view_config(route_name='home', renderer='templates/home.pt')
def my_view(request):
    return {'minAge': 5, 'maxAge': 50}


@view_config(renderer='json')
def search(request):
    mixAge = int(request.params.get('min', 0))
    maxAge = int(request.params.get('max', 100))

    return {}

import json

from pyramid.view import view_config

from loader import ArtistLoader
from searcher import ArtistSearcher


@view_config(route_name='home', renderer='templates/home.pt')
def home(request):
    return dict(minAge=5, maxAge=50)


@view_config(route_name='search', renderer='templates/search.pt')
def search(request):
    params = request.params.get('age').split(',')
    minAge = int(params[0])
    maxAge = int(params[1])

    json_path = '/home/otaviosoares/Projects/search-artist-challenge/src/search_artists/artists.json'
    artist_loader = ArtistLoader(json_path)
    searcher = ArtistSearcher(artist_loader.data['artists'])

    results = searcher.search_by_age(minAge, maxAge)
    artists_json = json.dumps(results, indent=4)

    return dict(artists=results, artists_json=artists_json, minAge=minAge, maxAge=maxAge)

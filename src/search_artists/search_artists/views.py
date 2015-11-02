import json

from pyramid.view import view_config
from pyramid.path import AssetResolver

from loader import ArtistLoader
from searcher import ArtistSearcher
from sorter import MedianSorter


@view_config(route_name='home', renderer='templates/home.pt')
def home(request):
    return dict()


@view_config(route_name='search', renderer='templates/search.pt')
def search(request):
    params = request.params.get('age').split(',')
    minAge = int(params[0])
    maxAge = int(params[1])

    asset_resolver = AssetResolver('search_artists')
    resolver = asset_resolver.resolve('data/artists.json')
    json_path = resolver.abspath()
    artist_loader = ArtistLoader(json_path)

    searcher = ArtistSearcher(artist_loader.data['artists'])
    results = searcher.search_by_age(minAge, maxAge, sorterKlass=MedianSorter)

    artists_json = json.dumps(results, indent=4)

    return dict(
        artists=results,
        artists_json=artists_json,
        minAge=minAge,
        maxAge=maxAge)

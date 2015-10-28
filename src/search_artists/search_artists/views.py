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

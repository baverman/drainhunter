import objgraph

from drainhunter import web
from drainhunter.core import snapshot, group_by_class

RETURN_DOT_FILE = False


def index(start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)

    return [web.index('/snapshot')[1]]

def take_snapshot(start_response):
    snapshot()
    status = '302 Moved temporarily'
    headers = [('Location', '/')]
    start_response(status, headers)

    return ''

def object_list(cls, start_response):
    status = '200 OK'
    for k, objects in group_by_class().iteritems():
        if k == cls:
            break
    else:
        headers = [('Content-type', 'text/html')]
        start_response(status, headers)

        return ['There are no any objects of class %s, try to refresh page later'
            ' or go to <a href="%s">index</a>.' % ( cls, '/')]

    if RETURN_DOT_FILE:
        objgraph.show_backrefs(objects, filename="/tmp/objgraph.dot")

        headers = [('Content-type', 'text/vnd.graphviz'),
            ('Content-Disposition', 'attachment; filename=objgraph.dot')]
        start_response(status, headers)

        return open('/tmp/objgraph.dot')

    objgraph.show_backrefs(objects)

    status = '302 Moved temporarily'
    headers = [('Location', '/')]
    start_response(status, headers)

    return ''


def drainhunter_app(environ, start_response):
    qs = environ['PATH_INFO']

    if qs.startswith('/snapshot'):
        return take_snapshot(start_response)

    if qs.startswith('/list') and qs.endswith('.dot'):
        cls = qs[6:][:-4]
        return object_list(cls, start_response)

    return index(start_response)

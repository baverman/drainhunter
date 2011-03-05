import subprocess
import objgraph

from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from drainhunter import snapshot, group_by_class

def index(request):
    objects = group_by_class()
    if not objects:
        return HttpResponse('There are no any new objects, wait and refresh the page')
    else:
        out = 'Take new <a href="%s">snapshot</a><br /><br />' % reverse('drainhunter-snapshot')

        for k, v in reversed(sorted(objects.items(), key=lambda r: len(r[1]))):
            out += '<a href="list/%s.dot">%s</a>: %d<br />' % (k, k, len(v))

        return HttpResponse(out)

def take_snapshot(request):
    snapshot()

    return HttpResponseRedirect(reverse('drainhunter-index'))

def object_list(request, cls, format):
    for k, objects in group_by_class().iteritems():
        if k == cls:
            break
    else:
        return HttpResponse('There are no any objects of class %s, try to refresh page later'
            ' or go to <a href="%s">index</a>.' % ( cls, reverse('drainhunter-index')))

    objgraph.show_backrefs(objects, filename="/tmp/objgraph.dot")
    if format == 'dot':
        response = HttpResponse(open('/tmp/objgraph.dot'), mimetype='text/vnd.graphviz')
        response['Content-Disposition'] = 'attachment; filename=objgraph.dot'
        return response
    elif format == 'png':
        return HttpResponse(open('/tmp/objgraph.png'), mimetype='image/png')

    convert_to_svg("/tmp/objgraph.dot", "/tmp/objgraph.svg")
    return HttpResponse(open('/tmp/objgraph.svg'), mimetype='image/svg+xml')

def convert_to_svg(filename, newfilename):
    dot = subprocess.Popen(['dot', '-Tsvg', '-o', newfilename, filename])
    dot.wait()

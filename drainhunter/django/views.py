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
            out += '<a href="list/%s">%s</a>: %d<br />' % (k, k, len(v))

        return HttpResponse(out)

def take_snapshot(request):
    snapshot()

    return HttpResponseRedirect(reverse('drainhunter-index'))

def object_list(request, cls):
    for k, objects in group_by_class().iteritems():
        if k == cls:
            break
    else:
        return HttpResponse('There are no any objects of class %s, try to refresh page later'
            ' or go to <a href="%s">index</a>.' % ( cls, reverse('drainhunter-index')))

    objgraph.show_backrefs(objects, filename="/tmp/objgraph.png")

    return HttpResponse(open('/tmp/objgraph.png'), mimetype='image/png')

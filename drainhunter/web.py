from drainhunter import group_by_class

def index(snapshot_url):
    objects = group_by_class()
    if not objects:
        return 404, 'There are no any new objects, wait and refresh the page'
    else:
        out = 'Take new <a href="%s">snapshot</a><br /><br />' % snapshot_url

        for k, v in reversed(sorted(objects.items(), key=lambda r: (len(r[1]), r[0]))):
            out += '<a href="list/%s.dot">%s</a>: %d<br />' % (k, k, len(v))

        return 200, out
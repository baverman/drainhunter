def run(port=9000):
    from wsgiref.simple_server import make_server
    import drainhunter.wsgi
    import threading

    httpd = make_server('', port, drainhunter.wsgi.drainhunter_app)

    thread = threading.Thread(target=httpd.serve_forever)
    thread.daemon = True
    thread.start()
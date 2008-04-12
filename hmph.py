from BaseHTTPServer import HTTPServer

import doss
import registry
import rest
import tests


server = None

def start():
    global server
    registry.load_system()
    server = HTTPServer(('', 8080), rest.HmphHTTPRequestHandler)
    print 'started httpserver...'
    serve()

def serve():
    server.serve_forever()

def main():
    try:
        start()
    except KeyboardInterrupt:
        print '^C received, shutting down server'
        server.socket.close()
        import os
        # XXX raises an exception in Windows if oldsnapshot exists
        # XXX should never overwrite old snapshots
        os.rename('snapshot.py', 'oldsnapshot')
        doss.serialize(registry.get_system(), file('snapshot.py', 'w'))

if __name__ == '__main__':
    # XXX do these tests after starting up the server, to minimize the
    # period when connections are refused after a restart.  Similarly for
    # importing the snapshot, etc.
    tests.tests()
    main()

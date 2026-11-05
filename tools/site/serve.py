"""The site, served with no caching, for testing:  python tools/site/serve.py [port]"""
import functools
import http.server
import sys
from pathlib import Path


class NoCache(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()

    def log_message(self, *args):
        pass


port = int(sys.argv[1]) if len(sys.argv) > 1 else 8335
site = str(Path(__file__).resolve().parents[2] / 'site')
http.server.ThreadingHTTPServer(('127.0.0.1', port), functools.partial(NoCache, directory=site)).serve_forever()

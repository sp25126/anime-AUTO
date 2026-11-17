import http.server
import socketserver
import urllib.parse
from google_auth_oauthlib.flow import InstalledAppFlow
import os

SCOPES = ['https://www.googleapis.com/auth/youtube.upload', 'https://www.googleapis.com/auth/youtube']
PORT = 8090
REDIRECT_URI = f"http://localhost:{PORT}/"

flow = InstalledAppFlow.from_client_secrets_file('config/client_secrets.json', SCOPES, redirect_uri=REDIRECT_URI)
auth_url, _ = flow.authorization_url(prompt='consent', access_type='offline')

with open("output/auth_link.txt", "w", encoding="utf-8") as f:
    f.write(auth_url)

print(f"AUTH_URL:{auth_url}", flush=True)

auth_code = None

class OAuthHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        global auth_code
        query = urllib.parse.urlparse(self.path).query
        params = urllib.parse.parse_qs(query)
        if 'code' in params:
            auth_code = params['code'][0]
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"<h1>Authorization successful! You can close this tab and return to Antigravity.</h1>")
        else:
            self.send_response(400)
            self.end_headers()

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", PORT), OAuthHandler) as httpd:
    print(f"Listening on localhost:{PORT}...", flush=True)
    while not auth_code:
        httpd.handle_request()

print("Fetching credentials token...", flush=True)
flow.fetch_token(code=auth_code)
creds = flow.credentials

with open("config/youtube_token.json", "w", encoding="utf-8") as f:
    f.write(creds.to_json())

print("SUCCESS: Token saved to config/youtube_token.json", flush=True)

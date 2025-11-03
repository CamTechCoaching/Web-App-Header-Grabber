import http.client  # For HTTP/HTTPS connections
from urllib.parse import urlparse  # To parse the URL

def get_http_headers(url):
    """Fetch and print HTTP headers for a given URL."""
    parsed = urlparse(url)                      # Break URL into components
    scheme = parsed.scheme or "http"            # e.g. 'http' or 'https'
    hostname = parsed.hostname                  # e.g. 'example.com'
    port = parsed.port                          # explicit port, if any

    # Use path + query, default to '/'
    path = parsed.path or "/"
    if parsed.query:
        path = path + "?" + parsed.query

    if not hostname:
        print("Error: invalid URL (missing hostname).")
        return

    # Choose connection type and default port
    if scheme == "https":
        conn = http.client.HTTPSConnection(hostname, port=port)  # default 443 if port None
    else:
        conn = http.client.HTTPConnection(hostname, port=port)   # default 80 if port None

    try:
        conn.request("GET", path)                # Send GET request
        response = conn.getresponse()            # Get response object

        print(f"HTTP Headers for {url}")
        for header, value in response.getheaders():  # Iterate headers
            print(f"{header}: {value}")

    except Exception as e:
        print("Error fetching headers:", e)
    finally:
        conn.close()  # Always close the connection

# ---------------- MAIN ---------------- #

# Example usage: change the URL or read from input
target_url = input("Enter a URL (include http:// or https://): ").strip() or "https://shodan.com"
get_http_headers(target_url)

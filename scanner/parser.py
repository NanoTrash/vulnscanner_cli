# scanner/parser.py

from urllib.parse import urlparse
from db.models import Host, Url


def extract_host_and_url(target_url, cursor):
    parsed = urlparse(target_url)
    hostname = parsed.hostname
    url = f"{parsed.scheme}://{parsed.netloc}"

    Host.insert(cursor, hostname=hostname, ip_address="")
    host_id = cursor.lastrowid

    Url.insert(cursor, host_id=host_id, url=url)
    url_id = cursor.lastrowid

    return host_id, url_id

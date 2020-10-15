import re

def domain_name(url):
    pattern = r'^(?:http(?:s?)://)?(?:www\.)?(.*?)\.(?:[a-z.-])'
    m = re.match(pattern, url)
    return m.group(1) if m else None
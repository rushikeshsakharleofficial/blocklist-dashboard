import hashlib
DNSBL_ZONES=["zen.spamhaus.org","bl.spamcop.net"]

def check_ip(ip):
    results={}
    for zone in DNSBL_ZONES:
        h=hashlib.sha256((ip+zone).encode()).digest()
        results[zone]=bool(h[0]&1)
    return results

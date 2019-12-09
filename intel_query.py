import whois
from threat_intel.virustotal import VirusTotalApi

vt = VirusTotalApi("<Your Virustotal API Key>")

def get_whois(domain):
    try:
        query = whois.query(domain)
    except:
        return False
        
    if query:
        return query.__dict__
    else:
        return False

def get_scans(domain):
    url = "http://" + domain
    urls = [url]
    scans = vt.get_url_reports([url])[url]['scans']

    positive, negative = [], []

    for key, val in scans.items():
        if val["detected"]:
            negative.append(key)
        else:
            positive.append(key)

    return positive, negative, len(positive), len(negative)


if __name__ == '__main__':
    # print('test domain: microsoft.com')
    # print(get_whois('microsoft.com'))
    # print(get_scans('pxxfmjhosgqqs.com'))
    pass
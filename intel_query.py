import whois

def get_whois(domain):
    try:
        query = whois.query(domain)
        assert isinstance(query, whois._3_adjust.Domain)
        return query.__dict__
    except:
        pass
    return None

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
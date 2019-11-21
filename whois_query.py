import whois

def get_whois(domain):
    query = whois.query(domain)
    if query:
        return query.__dict__
    else:
        return False

if __name__ == '__main__':
    print('test domain: microsoft.com')
    print(get_whois('microsoft.com'))
import dns.resolver
from library.miscellaneous import get_datetime_now, convert_to_json
from library.apicalls import send_data

def get_dns_record_a(domain, dns_server="4.2.2.2", client=0):
    a_records = {}
    a_records["client"] = client
    a_records["domain"] = domain
    a_records["dns_server"] = dns_server
    a_records["date_time"] = get_datetime_now()
    _a = []
    resolver = dns.resolver.Resolver(configure=False)
    resolver.nameservers = [dns_server]
    try:
        result = resolver.resolve(domain, "A")
    except Exception as e:
        a_records["response"] = False
        a_records["reason"] = f"{str(e)}"
    else:
        a_records["response"] = True
        for rdata in result.rrset:
            _a.append(rdata.to_text())
        a_records["a_records"] = []
        a_records["a_records"] += _a
    adns_json = convert_to_json(a_records)
    resultado = send_data(adns_json,"adnsrecord")
    return resultado

def get_dns_record_mx(domain, dns_server="4.2.2.2", client=0):
    """
    Function receives a domain and a optional dns server for query MX DNS records
    it returns a dictionary with mx_recods and a result variable.
    """
    mx_records = {}
    mx_records["domain"] = domain
    mx_records["client"] = client
    mx_records["dns_server"] = dns_server
    mx_records["date_time"] = get_datetime_now()
    _mx = {}
    mx = 1
    records = {}
    resolver = dns.resolver.Resolver(configure=False)
    resolver.nameservers = [dns_server]
    try:
        result = resolver.resolve(domain, "MX")
    except Exception as e:
        mx_records["response"] = False
        mx_records["reason"] = f"{str(e)}"
    else:
        mx_records["response"] = True
        for rdata in result.rrset:
            _mm = rdata.to_text().split()
            _mx["priority"] = _mm[0]
            _mx["exchanger_svr"] = _mm[1]
            records["exchanger" + str(mx)] = _mx
            mx += 1
        mx_records["mx_records"] = records
    mxdns_json = convert_to_json(mx_records)
    resultado = send_data(mxdns_json,"mxdnsrecord")
    return resultado


def get_dns_record_ns(domain, dns_server="4.2.2.2", client=0):
    ns_records = {}
    ns_records["domain"] = domain
    ns_records["dns_server"] = dns_server
    ns_records["date_time"] = get_datetime_now()
    ns_records["client"] = client
    _ns = []
    resolver = dns.resolver.Resolver(configure=False)
    resolver.nameservers = [dns_server]
    try:
        result = resolver.resolve(domain, "NS")
    except Exception as e:
        ns_records["response"] = False
        ns_records["reason"] = f"{str(e)}"
    else:
        ns_records["response"] = True
        for rdata in result.rrset:
            _ns.append(rdata.to_text())
        ns_records["ns_records"] = []
        ns_records["ns_records"] += _ns
    nsdns_json = convert_to_json(ns_records)
    resultado = send_data(nsdns_json,"nsdnsrecord")
    return resultado

def get_dns_record_soa(domain, dns_server="4.2.2.2", client=0):
    soa_records = {}
    soa_records["domain"] = domain
    soa_records["dns_server"] = dns_server
    soa_records["date_time"] = get_datetime_now()
    soa_records["client"] = client
    records = {}
    resolver = dns.resolver.Resolver(configure=False)
    resolver.nameservers = [dns_server]
    try:
        result = resolver.resolve(domain, "SOA")
    except Exception as e:
        soa_records["response"] = False
        soa_records["reason"] = f"{str(e)}"
    else:
        soa_records["response"] = True
        _soa = result.rrset.to_text().split()
        records["primary_ns"] = _soa[4]
        records["responsible_mail_address"] = _soa[5]
        records["serial"] = _soa[6]
        records["refresh"] = _soa[7]
        records["retry"] = _soa[8]
        records["expire"] = _soa[9]
        records["default_ttl"] = _soa[10]
    soa_records["soa_records"] = records
    soa_json = convert_to_json(soa_records)
    resultado = send_data(soa_json,"soadnsrecord")
    return resultado


def get_dns_record_txt(domain, dns_server="4.2.2.2", client=0):
    txt_records = {}
    _txt = []
    txt_records["domain"] = domain
    txt_records["dns_server"] = dns_server
    txt_records["date_time"] = get_datetime_now()
    txt_records["client"] = client
    resolver = dns.resolver.Resolver(configure=False)
    resolver.nameservers = [dns_server]
    try:
        result = resolver.resolve(domain, "TXT")
    except Exception as e:
        txt_records["response"] = False
        txt_records["reason"] = f"{str(e)}"

    else:
        txt_records["response"] = True
        for rdata in result.rrset:
            _txt.append(rdata.to_text().strip('"'))
            txt_records["txt_records"] = []
            txt_records["txt_records"] += _txt
    txt_json = convert_to_json(txt_records)
    print (txt_json)
    resultado = send_data(txt_json,"txtdnsrecord")
    return resultado
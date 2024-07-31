from certifier import CertInfo


def get_cert_info(host, port=443):
    cert_records = {}
    cert = CertInfo(host, port)
    try:
        cert.info()
    except Exception as e:
        cert_records["result"] = False
        cert_records["reason"] = f"{str(e)}"
    else:
        cert_records["result"] = True
        cert_records["Session_stats"] = cert.session_stats()
        cert_records["cert_stats"] = cert.cert_stats()
        cert_records["cipher"] = cert.cipher()
        cert_records["expire"] = cert.expire()
        cert_records["protocol"] = cert.protocol()
        info = cert.info()
        cert_records["notBefore"] = info["notBefore"]
        cert_records["issuer"] = info["issuer"][1][0][1]
    return cert_records


print(get_cert_info("netheads.com.mx"))

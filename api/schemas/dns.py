def AdnsEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "client": item["client"],
        "domain": item["domain"],
        "a_records": item ["a_records"],
        "date_time": item["date_time"],
        "dns_server" : item["dns_server"],
        "reason":item["reason"]
    } 

def AdnsEntities(entity) -> list:
    return [AdnsEntity (item) for item in entity]

def MXdnsEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "client": item["client"],
        "response": item["response"],
        "mx_records": item["mx_records"],
        "domain": item["domain"],
        "dns_server": item["dns_server"],
        "date_time": item["date_time"],
        "reason":item["reason"]
    }

def MXdnsEntities(entity) -> list:
    return [MXdnsEntity (item) for item in entity]

def NSdnsEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "client": item["client"],
        "response": item["response"],
        "ns_records": item["ns_records"],
        "domain": item["domain"],
        "dns_server": item["dns_server"],
        "date_time": item["date_time"],
        "reason":item["reason"]
    }

def NSdnsEntities(entity) -> list:
    return [NSdnsEntity (item) for item in entity]

def SOAdnsEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "client": item["client"],
        "response": item["response"],
        "soa_records": item["soa_records"],
        "domain": item["domain"],
        "dns_server": item["dns_server"],
        "date_time": item["date_time"],
        "reason":item["reason"]
    }

def SOAdnsEntities(entity) -> list:
    return [SOAdnsEntity (item) for item in entity]


def TXTdnsEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "client": item["client"],
        "response": item["response"],
        "txt_records": item["txt_records"],
        "domain": item["domain"],
        "dns_server": item["dns_server"],
        "date_time": item["date_time"],
        "reason":item["reason"]
    }

def TXTdnsEntities(entity) -> list:
    return [TXTdnsEntity (item) for item in entity]
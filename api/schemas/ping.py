def pingEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "client": item["client"],
        "hostname": item["hostname"],
        "response": item["response"],
        "date_time": item["date_time"],
        "reason": item["reason"],
        "rtt_max_avg": item["rtt_max_avg"],
        "rtt_min_ms": item["rtt_min_ms"],
        "rtt_max": item["rtt_max"],
        "rtt_min": item["rtt_min"],
        "rtt_max_ms": item["rtt_max_ms"],
        "packets_sent": item["packets_sent"],
        "packets_received": item["packets_received"]
    }

def pingsEntity(entity) -> list:
    return [pingEntity (item) for item in entity]
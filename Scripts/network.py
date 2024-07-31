from pythonping import ping
from library.miscellaneous import get_datetime_now, convert_to_json
from library.apicalls import send_data

def basic_ping(host, timeout=2, count=5, interval=5):
    """
    Make ping test to remote host. Function takes at least the domain as parameter.
    By default the monitor will send 5 pings with 5 seconds between them.
    Failure is considered by default after 2 seconds.
    Function return a dictionary with all stats from the ping or a error message.
    """
    
    ping_response = {
        "date_time": get_datetime_now()
    }
    
    try:
        response = ping(host, timeout=timeout, count=count, interval=interval)
    except:
        ping_response["response"] = False
        ping_response["reason"] = "Impossible to resolve the domain name."
        return ping_response
    else:
        if response.success() == True:
            ping_response["client"] = 0
            ping_response["hostname"] = host
            ping_response["response"] = True
            ping_response["rtt_avg"] = response.rtt_avg
            ping_response["rtt_min_ms"] = response.rtt_min_ms
            ping_response["rtt_max"] = response.rtt_max
            ping_response["rtt_min"] = response.rtt_min
            ping_response["rtt_max_ms"] = response.rtt_max_ms
            ping_response["packets_sent"] = response.stats_packets_sent
            ping_response["packets_received"] = response.stats_packets_returned
            ping_json = convert_to_json(ping_response)
            resultado = send_data(ping_json,"ping")
            return resultado
        else:
            ping_response["response"] = False
            ping_response["reason"] = "Ping disabled or host unreachable."
            return ping_response

    
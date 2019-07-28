"""
Get the data from whereever and create the JSON blob
"""


BLOB = {
    "machine_id": "",
    "ls": {
        "files": 3,
        "extensions": [1,2,3],
        "size": {"1": 0.3, "2": 0.3, "3": 0.4},
        "raw": "aaaa"},
    "netstat": {
        "ports": 0,
        "protocol": [3, 2],
        "state": [{"LISTEN": 1}],
        "raw": "aaaa"},
    "ps": {
        "number": 10,
        "top_3": [10, 10, 10],
        "frequency": [{"9815": 0.5, "10136": 0.5}],
        "raw": "aaaa"},

    "nmap": {
        "runtime": "4.1",
        "latency": "10,11,17",
        "ips": [{
            "10.123.0.2": 0.25,
            "10.123.0.2": 0.25,
            "10.123.0.2": 0.25,
            "10.123.0.2": 0.25}],
        "raw": "aaaa"},
    "keylogging": {
        "last_hour": 100,
        "last_3_days": [100,200,300],
        "frequency": [{"a": 0.1},{"b":0.9}],
        "raw": "abababbababbababa"},
}


def parse_nstat(yuuvis_data, machine_id, data_type):
    BLOB[data_type]["raw"] = yuuvis_data
    BLOB[machine_id] = machine_id



def parse_machine(machine_id, yuuvis_data, data_type):
    parse_nstat(yuuvis_data, machine_id, data_type)

    return BLOB




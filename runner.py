from queryy import get_object_yuuvis, get_data_yuuvis
from parser import parse_machine


def runner(machine_id, data_type):
    blob_data = get_object_yuuvis(machine_id, data_type)
    file_data = get_data_yuuvis(blob_data).text
    return parse_machine(machine_id, file_data)


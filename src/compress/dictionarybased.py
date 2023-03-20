import json
import gzip


def dict_encode(data):
    """
    Compresses a dictionary using GZIP compression.
    """
    json_data = json.dumps(data).encode('utf-8')
    compressed_data = gzip.compress(json_data)
    return compressed_data


def dict_decode(data):
    """
    Decompresses a dictionary that has been compressed using GZIP.
    """
    decompressed_data = gzip.decompress(data)
    json_data = decompressed_data.decode('utf-8')
    return json.loads(json_data)

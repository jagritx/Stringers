from collections import Counter


def cabac_encode(s):
    freqs = Counter(s)
    total_freq = sum(freqs.values())
    freqs = {char: freq / total_freq for char, freq in freqs.items()}
    ranges = {}
    lower_bound = 0
    for char, prob in freqs.items():
        upper_bound = lower_bound + prob
        ranges[char] = (lower_bound, upper_bound)
        lower_bound = upper_bound
    start_range = 0
    end_range = 1
    for char in s:
        char_range = ranges[char]
        range_size = end_range - start_range
        start_range += range_size * char_range[0]
        end_range = start_range + range_size * (char_range[1] - char_range[0])

    return (start_range, end_range)


def cabac_decode(encoded, length, freqs):
    total_freq = sum(freqs.values())
    freqs = {char: freq / total_freq for char, freq in freqs.items()}
    ranges = {}
    lower_bound = 0
    for char, prob in freqs.items():
        upper_bound = lower_bound + prob
        ranges[char] = (lower_bound, upper_bound)
        lower_bound = upper_bound
    start_range = 0
    end_range = 1
    decoded = ''
    for i in range(length):
        range_size = end_range - start_range
        for char, char_range in ranges.items():
            if start_range + range_size * char_range[0] <= encoded < start_range + range_size * char_range[1]:
                decoded += char
                start_range += range_size * char_range[0]
                end_range = start_range + range_size * \
                    (char_range[1] - char_range[0])
                break

    return decoded

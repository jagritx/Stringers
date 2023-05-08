def sf_encode(symbol_frequencies):
    """
    Encodes a dictionary of symbol frequencies using the Shannon-Fano algorithm.
    Returns a dictionary of codewords for each symbol.
    """
    # Sort symbols by decreasing frequency
    sorted_symbols = sorted(symbol_frequencies.items(),
                            key=lambda x: x[1], reverse=True)

    # Divide symbols into two sets with as close to equal total frequency as possible
    set_1 = []
    set_2 = []
    set_1_total_freq = 0
    set_2_total_freq = 0
    for symbol, freq in sorted_symbols:
        if set_1_total_freq <= set_2_total_freq:
            set_1.append(symbol)
            set_1_total_freq += freq
        else:
            set_2.append(symbol)
            set_2_total_freq += freq

    # Generate codewords recursively
    codewords = {}
    if len(set_1) == 1:
        codewords[set_1[0]] = '0'
    else:
        set_1_codewords = sf_encode(
            {symbol: symbol_frequencies[symbol] for symbol in set_1})
        for symbol, codeword in set_1_codewords.items():
            codewords[symbol] = '0' + codeword

    if len(set_2) == 1:
        codewords[set_2[0]] = '1'
    else:
        set_2_codewords = sf_encode(
            {symbol: symbol_frequencies[symbol] for symbol in set_2})
        for symbol, codeword in set_2_codewords.items():
            codewords[symbol] = '1' + codeword

    return codewords

#  Copyright (c) 2022. Illia Popov.

def rotate_left(n, b):
    return ((n << b) | (n >> (32 - b))) & 0xffffffff


def message_padding(message):
    # Pad the message
    message = ''.join(format(ord(x), 'b').zfill(8) for x in message)
    start_message_length = len(message)

    message += '1'

    while (len(message) % 512) != 448:
        message += '0'

    message_length_binary = bin(start_message_length)[2:].zfill(64)
    message += message_length_binary

    return message


def sha1_hash(message):

    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    message_padded = message_padding(message)
    message_chunks = [message_padded[i:i + 512] for i in range(0, len(message_padded), 512)]

    for chunk in message_chunks:
        a = h0
        b = h1
        c = h2
        d = h3
        e = h4

        w = [int(chunk[i:i + 32], 2) for i in range(0, len(chunk), 32)]

        for t in range(16, 80):
            w.append(rotate_left((w[t - 3] ^ w[t - 8] ^ w[t - 14] ^ w[t - 16]), 1))

        for t in range(80):

            if t <= 19:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif 20 <= t <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= t <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            elif 60 <= t <= 79:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = (rotate_left(a, 5) + f + e + k + w[t]) & 0xffffffff
            e = d
            d = c
            c = rotate_left(b, 30)
            b = a
            a = temp

        h0 = (h0 + a) & 0xffffffff
        h1 = (h1 + b) & 0xffffffff
        h2 = (h2 + c) & 0xffffffff
        h3 = (h3 + d) & 0xffffffff
        h4 = (h4 + e) & 0xffffffff

    return f'{hex(h0)[2:].zfill(8)}{hex(h1)[2:].zfill(8)}{hex(h2)[2:].zfill(8)}{hex(h3)[2:].zfill(8)}{hex(h4)[2:].zfill(8)}'


if __name__ == '__main__':
    print(sha1_hash(input()))

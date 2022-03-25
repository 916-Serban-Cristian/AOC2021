def skip_literal():
    global packet
    group = packet[:5]
    packet = packet[5:]
    literal_length = 5
    first_bit = group[0]
    while first_bit == '1':
        group = packet[:5]
        packet = packet[5:]
        literal_length += 5
        first_bit = group[0]
    return literal_length


def skip_subpackets_by_length(length):
    global packet, version_sum
    nr_skipped = 0
    while length:
        version = int(packet[:3], 2)
        version_sum += version
        packet = packet[3:]
        length -= 3
        type_id = int(packet[:3], 2)
        packet = packet[3:]
        length -= 3
        if type_id == 4:
            length -= skip_literal()
            nr_skipped += 1
        else:
            length_type_id = packet[0]
            packet = packet[1:]
            length -= 1
            if length_type_id == '0':
                subpacket_length = int(packet[:15], 2)
                packet = packet[15:]
                length -= 15
                skip_subpackets_by_length(subpacket_length)
                nr_skipped += 1
                length -= subpacket_length
            elif length_type_id == '1':
                subpacket_count = int(packet[:11], 2)
                packet = packet[11:]
                length -= 11
                length -= skip_subpackets_by_count(subpacket_count)
                nr_skipped += 1
    return nr_skipped


def skip_subpackets_by_count(count):
    global packet, version_sum
    subpackets_length = 0
    while count:
        version = int(packet[:3], 2)
        version_sum += version
        packet = packet[3:]
        subpackets_length += 3
        type_id = int(packet[:3], 2)
        packet = packet[3:]
        subpackets_length += 3
        if type_id == 4:
            subpackets_length += skip_literal()
            count -= 1
        else:
            length_type_id = packet[0]
            packet = packet[1:]
            subpackets_length += 1
            if length_type_id == '0':
                subpacket_length = int(packet[:15], 2)
                packet = packet[15:]
                skip_subpackets_by_length(subpacket_length)
                count -= 1
                subpackets_length += (subpacket_length + 15)
            elif length_type_id == '1':
                subpacket_count = int(packet[:11], 2)
                packet = packet[11:]
                subpackets_length += (skip_subpackets_by_count(subpacket_count) + 11)
                count -= 1
    return subpackets_length


with open('input.txt', 'r') as f:
    hex_packet = f.read()
hex_dict = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
            '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
packet = ''.join(list(map(lambda x: hex_dict[x], hex_packet)))
version_sum = 0
while len(packet):
    version = int(packet[:3], 2)
    version_sum += version
    packet = packet[3:]
    type_id = int(packet[:3], 2)
    packet = packet[3:]
    if type_id == 4:
        skip_literal()
    else:
        length_type_id = packet[0]
        packet = packet[1:]
        if length_type_id == '0':
            subpacket_length = int(packet[:15], 2)
            packet = packet[15:]
            skip_subpackets_by_length(subpacket_length)
        elif length_type_id == '1':
            subpacket_count = int(packet[:11], 2)
            packet = packet[11:]
            skip_subpackets_by_count(subpacket_count)
    if len(packet) == packet.count('0'):
        break
print(version_sum)

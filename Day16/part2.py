from math import prod


def process_literal():
    global packet
    group = packet[:5]
    packet = packet[5:]
    literal_length = 5
    literal_value = group[1:]
    first_bit = group[0]
    while first_bit == '1':
        group = packet[:5]
        packet = packet[5:]
        literal_length += 5
        literal_value = literal_value + group[1:]
        first_bit = group[0]
    return literal_length, int(literal_value, 2)


def process_subpackets_by_length(length):
    global packet, value_stack
    nr_skipped = 0
    while length:
        packet = packet[3:]
        length -= 3
        type_id = int(packet[:3], 2)
        packet = packet[3:]
        length -= 3
        if type_id == 4:
            literal_length, literal_value = process_literal()
            value_stack.append(literal_value)
            length -= literal_length
            nr_skipped += 1
        else:
            length_type_id = packet[0]
            packet = packet[1:]
            length -= 1
            if length_type_id == '0':
                subpacket_length = int(packet[:15], 2)
                packet = packet[15:]
                length -= 15
                subpacket_count = process_subpackets_by_length(subpacket_length)
                nr_skipped += 1
                length -= subpacket_length
            else:
                subpacket_count = int(packet[:11], 2)
                packet = packet[11:]
                length -= 11
                length -= process_subpackets_by_count(subpacket_count)
                nr_skipped += 1
            if type_id == 0:
                s = sum(value_stack[-subpacket_count:])
                value_stack = value_stack[:-subpacket_count]
                value_stack.append(s)
            elif type_id == 1:
                p = prod(value_stack[-subpacket_count:])
                value_stack = value_stack[:-subpacket_count]
                value_stack.append(p)
            elif type_id == 2:
                m = min(value_stack[-subpacket_count:])
                value_stack = value_stack[:-subpacket_count]
                value_stack.append(m)
            elif type_id == 3:
                m = max(value_stack[-subpacket_count:])
                value_stack = value_stack[:-subpacket_count]
                value_stack.append(m)
            elif type_id == 5:
                y = value_stack.pop()
                x = value_stack.pop()
                value_stack.append(int(x > y))
            elif type_id == 6:
                y = value_stack.pop()
                x = value_stack.pop()
                value_stack.append(int(x < y))
            elif type_id == 7:
                y = value_stack.pop()
                x = value_stack.pop()
                value_stack.append(int(x == y))
    return nr_skipped


def process_subpackets_by_count(count):
    global packet, value_stack
    subpackets_length = 0
    while count:
        packet = packet[3:]
        subpackets_length += 3
        type_id = int(packet[:3], 2)
        packet = packet[3:]
        subpackets_length += 3
        if type_id == 4:
            literal_length, literal_value = process_literal()
            value_stack.append(literal_value)
            subpackets_length += literal_length
            count -= 1
        else:
            length_type_id = packet[0]
            packet = packet[1:]
            subpackets_length += 1
            if length_type_id == '0':
                subpacket_length = int(packet[:15], 2)
                packet = packet[15:]
                subpacket_count = process_subpackets_by_length(subpacket_length)
                count -= 1
                subpackets_length += (subpacket_length + 15)
            else:
                subpacket_count = int(packet[:11], 2)
                packet = packet[11:]
                subpackets_length += (process_subpackets_by_count(subpacket_count) + 11)
                count -= 1
            if type_id == 0:
                s = sum(value_stack[-subpacket_count:])
                value_stack = value_stack[:-subpacket_count]
                value_stack.append(s)
            elif type_id == 1:
                p = prod(value_stack[-subpacket_count:])
                value_stack = value_stack[:-subpacket_count]
                value_stack.append(p)
            elif type_id == 2:
                m = min(value_stack[-subpacket_count:])
                value_stack = value_stack[:-subpacket_count]
                value_stack.append(m)
            elif type_id == 3:
                m = max(value_stack[-subpacket_count:])
                value_stack = value_stack[:-subpacket_count]
                value_stack.append(m)
            elif type_id == 5:
                y = value_stack.pop()
                x = value_stack.pop()
                value_stack.append(int(x > y))
            elif type_id == 6:
                y = value_stack.pop()
                x = value_stack.pop()
                value_stack.append(int(x < y))
            elif type_id == 7:
                y = value_stack.pop()
                x = value_stack.pop()
                value_stack.append(int(x == y))
    return subpackets_length


with open('input.txt', 'r') as f:
    hex_packet = f.read()
hex_dict = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
            '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
packet = ''.join(list(map(lambda x: hex_dict[x], hex_packet)))
value_stack = []
while len(packet):
    packet = packet[3:]
    type_id = int(packet[:3], 2)
    packet = packet[3:]
    if type_id == 4:
        literal_length, literal_value = process_literal()
        value_stack.append(literal_value)
    else:
        length_type_id = packet[0]
        packet = packet[1:]
        if length_type_id == '0':
            subpacket_length = int(packet[:15], 2)
            packet = packet[15:]
            process_subpackets_by_length(subpacket_length)
        elif length_type_id == '1':
            subpacket_count = int(packet[:11], 2)
            packet = packet[11:]
            process_subpackets_by_count(subpacket_count)
        if type_id == 0:
            s = sum(value_stack)
            value_stack = [s]
        elif type_id == 1:
            p = prod(value_stack)
            value_stack = [p]
        elif type_id == 2:
            m = min(value_stack)
            value_stack = [m]
        elif type_id == 3:
            m = max(value_stack)
            value_stack = [m]
        elif type_id == 5:
            y = value_stack.pop()
            x = value_stack.pop()
            value_stack.append(int(x > y))
        elif type_id == 6:
            y = value_stack.pop()
            x = value_stack.pop()
            value_stack.append(int(x < y))
        elif type_id == 7:
            y = value_stack.pop()
            x = value_stack.pop()
            value_stack.append(int(x == y))
    if len(packet) == packet.count('0'):
        break
print(value_stack[0])

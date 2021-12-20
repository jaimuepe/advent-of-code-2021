
import my_io

input = my_io.get_clipboard_contents()

lines = input.splitlines()


class Packet:
    def __init__(self):
        self.version: str = ''
        self.type_id: str = ''

    def GetValue(self):
        return None


class LiteralPacket(Packet):
    def __init__(self):
        super().__init__()
        self.value = -1

    def GetValue(self):
        return self.value


class OperatorPacket(Packet):
    def __init__(self):
        self.sub_packets: list[Packet] = []

    def GetValue(self):
        if self.type_id == 0:
            return self.Sum()
        if self.type_id == 1:
            return self.Prod()
        if self.type_id == 2:
            return self.Min()
        if self.type_id == 3:
            return self.Max()
        if self.type_id == 5:
            return self.Gt()
        if self.type_id == 6:
            return self.Lt()
        if self.type_id == 7:
            return self.Eq()
        return 0

    def Sum(self):
        sum = 0
        for sub_packet in self.sub_packets:
            sum += sub_packet.GetValue()
        return sum

    def Prod(self):
        prod = 1
        for sub_packet in self.sub_packets:
            prod *= sub_packet.GetValue()
        return prod

    def Min(self):
        m = float('inf')
        for sub_packet in self.sub_packets:
            m = min(m, sub_packet.GetValue())
        return m

    def Max(self):
        m = float('-inf')
        for sub_packet in self.sub_packets:
            m = max(m, sub_packet.GetValue())
        return m

    def Gt(self):
        v1 = self.sub_packets[0].GetValue()
        v2 = self.sub_packets[1].GetValue()

        return 1 if v1 > v2 else 0

    def Lt(self):
        v1 = self.sub_packets[0].GetValue()
        v2 = self.sub_packets[1].GetValue()

        return 1 if v1 < v2 else 0

    def Eq(self):
        v1 = self.sub_packets[0].GetValue()
        v2 = self.sub_packets[1].GetValue()

        return 1 if v1 == v2 else 0


class Sequence:
    def __init__(self, binary_sequence: str):
        self.last_index = 0
        self.binary_sequence = binary_sequence

    def Take(self, amount: int) -> str:
        ret = self.binary_sequence[self.last_index:self.last_index + amount]
        self.last_index += amount
        return ret

    def TakeInt(self, amount: int) -> int:
        return int(self.Take(amount), 2)

    def Parse(self) -> Packet:
        return self.TakePackage()

    def TakePackage(self):

        packet_version = self.TakeInt(3)
        packet_type_id = self.TakeInt(3)

        if packet_type_id == 4:
            packet = self.CreateLiteralPacket(packet_version)
        else:
            packet = self.CreateOperatorPacket(packet_version, packet_type_id)

        return packet

    def CreateOperatorPacket(self, packet_version, packet_type_id) -> OperatorPacket:
        mode = self.TakeInt(1)

        packet = OperatorPacket()
        packet.type_id = packet_type_id
        packet.version = packet_version

        if mode == 0:
            length = self.TakeInt(15)
            sub_sequence = Sequence(self.Take(length))
            while sub_sequence.last_index < length:
                packet.sub_packets.append(sub_sequence.TakePackage())
        else:
            amount = self.TakeInt(11)
            for i in range(0, amount):
                packet.sub_packets.append(self.TakePackage())

        return packet

    def CreateLiteralPacket(self, packet_version) -> LiteralPacket:
        binary_str = ''
        while True:
            prefix = self.TakeInt(1)
            binary_str += self.Take(4)
            if prefix == 0:
                break

        literal_num = int(binary_str, 2)

        packet = LiteralPacket()
        packet.version = packet_version
        packet.type_id = 4
        packet.value = literal_num

        return packet


map = dict()
map['0'] = '0000'
map['1'] = '0001'
map['2'] = '0010'
map['3'] = '0011'
map['4'] = '0100'
map['5'] = '0101'
map['6'] = '0110'
map['7'] = '0111'
map['8'] = '1000'
map['9'] = '1001'
map['A'] = '1010'
map['B'] = '1011'
map['C'] = '1100'
map['D'] = '1101'
map['E'] = '1110'
map['F'] = '1111'

line = lines[0]

binary_string = ''.join([map[x] for x in line])

seq = Sequence(binary_string)

packet = seq.Parse()

print(packet.GetValue())

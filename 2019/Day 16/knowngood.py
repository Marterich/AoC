import math, sys

INPUTS = [
        '03036732577212944063491565474664',
        '02935109699940807407585447034323',
        '03081770884921959731165446850517',
        '59796332430280528211060657577039744056609636505111313336094865900635343682296702094018432765613019371234483818415934914575717134617783515237300919201989706451524069044921384738930172026234872525254689609787752401342687098918804210494391161531008341329016626922990938854681575317559821067933058630688365067790812341475168200215494963690593873250884807840611487288560291748414160551508979374335267106414602526249401281066501677212002980616711058803845336067123298983258010079178111678678796586176705130938139337603538683803154824502761228184209473344607055926120829751532887810487164482307564712692208157118923502010028250886290873995577102178526942152'
        ]

EXPECTED_OUTPUTS = [
        (100, '84462026'),
        (100, '78725270'),
        (100, '53553731'),
        (100, '79723033')
        ]

class FFT:
    BASE_PATTERN = [1, 0, -1, 0]
    MULTIPLIER = 10000
    NUM_OFFSET_DIGITS = 7
    MESSAGE_SIZE = 8

    def __init__(self, input_data):
        message_offset = int(input_data[:self.NUM_OFFSET_DIGITS])
        input_data = [int(d) for d in input_data]
        data_length = len(input_data) * self.MULTIPLIER
        assert message_offset > data_length / 2,\
        'There is no fast way to solve this'
        necessary_length = data_length - message_offset 
        num_copies = math.ceil(necessary_length / len(input_data))
        input_data = input_data * num_copies
        self.input_data = input_data[-necessary_length:]

    def get_message(self, num_phases):
        output = self._calculate(num_phases)
        message = ''.join([str(d) for d in output[:self.MESSAGE_SIZE]])
        return message

    def _calculate(self, num_phases):
        data = self.input_data
        for i in range(0, num_phases):
            sum = 0
            for j in range(len(data) - 1, -1, -1):
                sum += data[j]
                data[j] = sum % 10
        return data

def get_output(input_index, num_phases):
    input_data = INPUTS[input_index]
    fft = FFT(input_data)
    return fft.get_message(num_phases)

def main():
    if sys.argv[1] == 'test':
        success = True
        for i in range(len(INPUTS)):
            expected_output = EXPECTED_OUTPUTS[i][1]
            output = get_output(i, EXPECTED_OUTPUTS[i][0])
            output = output[:len(expected_output)]
            if output != expected_output:
                success = False
                print(f'Test {i} failed Expected: {expected_output} '
                    f'Actual: {output}')
        if success:
            print(f'{len(INPUTS)} tests passed')
    else:
        input_index = int(sys.argv[1])
        num_phases = int(sys.argv[2])
        output = get_output(input_index, num_phases)
        print(f'The message after {num_phases} phases is {output}')

if __name__ == '__main__':
    main()
# python standard library
import uuid
import random
# python external library
import ulid

class SomeId:

    @staticmethod
    def create_uuid(version: int=4):
        if version == 1:
            return str(uuid.uuid1())
        elif version == 4:
            return str(uuid.uuid4())
        else:
            raise ValueError('Version: {} is invalid'.format(version))

    @staticmethod
    def create_ulid():
        # 26文字生成する
        return ulid.new().str

    @staticmethod
    def create_randid(n: int=20, with_symbol=True):
        materials = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
        ]
        symbol = [
            '-', '=', '^', '~', '|', '@', '`', '[', ']', '{', '}', ';', '+',
            ':', '*', '<', '>', ',', '.', '/', '?', '_', '!', '#', '$', '%',
            '&', '(', ')'
        ]
        if with_symbol:
            return ''.join(random.choices(materials+symbol, k=n))
        else:
            return ''.join(random.choices(materials, k=n))



if __name__ == '__main__':
    print('UUID-1: {}'.format(SomeId.create_uuid(version=1)))
    print('UUID-4: {}'.format(SomeId.create_uuid()))
    print('ULID: {}'.format(SomeId.create_ulid()))
    print('RANDOM-ID: {}'.format(SomeId.create_randid(n=100, with_symbol=True)))
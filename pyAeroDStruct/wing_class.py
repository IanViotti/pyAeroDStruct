

class Wing():
    def __init__(self, b):
        # Checking span
        if not isinstance(b, float) or not b > 0 :
            raise ValueError(
                'span must be of type float and a positive number'
                )   

        self.__b = b

    def __repr__(self):
        repr1 = 'Wing parameters \n'
        repr2 = f'Span: {b}'
        return repr1 + repr2



if __name__ == '__main__':
    b = 2.4
    wing1 = Wing(b)
    print(wing1)
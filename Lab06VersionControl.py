#Tanner Fulwider's Program

def encode(password):
    res = ''
    for item in password:
        num = str(int(item) + 3)
        if len(num) == 2:
            num = num[1]
        res += num
    return res

def decode(encoded_password):
    original =''
    for element in encoded_password:
        num = (int(element) - 3)
        if num < 0:
            original += str(num + 10)
        else:
            original += str(num)
    return original

def main():
    coder_continue = True
    while coder_continue:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        option = int(input('\nPlease enter an option: '))
        if option == 1:
            decoded_pass = input('Please enter your password to encode: ')
            encoded_password = encode(decoded_pass)
            print('Your password has been encoded and stored!')
            print()
        if option == 2:
            new_decoded_pass = decode(encoded_password)
            print(f'The encoded password is {encoded_password}, and the original password is {new_decoded_pass}.')
        if option == 3:
            coder_continue = False
            break

if __name__ == '__main__':
    main()

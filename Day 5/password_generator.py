from random import choice

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "+", "-", "=", ".", ",", "~", "^", "[", "]", "{", "}", "(",")", ";",":", "<",">"]

print("Welcome to the password generator! Follow the steps below to generate your new password")
print("First, how do you want to generate your new password?")
print("1 - Totally random")
print("2 - Guided generator")
pass_option = input("Type 1 or 2: \n")

def random_password(pass_length, letters_qt, symbols_qt, numbers_qt):
    password = ""
    password_letters = []
    password_symbols = []
    password_numbers = []
    for n in range(letters_qt):
        new_letter = choice(letters)
        is_capital = choice([True, False])
        if is_capital:
            new_letter = new_letter.upper()
        password_letters.append(new_letter)
    for n in range(symbols_qt):
        new_symbol = choice(symbols)
        password_symbols.append(new_symbol)
    for n in range(numbers_qt):
        new_number = choice(numbers)
        password_numbers.append(new_number)
    char_options = password_letters + password_symbols + password_numbers
    for character in range(1, pass_length + 1):
        char_to_add = choice(char_options)
        char_options.remove(char_to_add)
        password += char_to_add
    return password


while True:
    if pass_option == "1":
        password_length = choice(range(6, 26))
        char_input = 0
        numbers_input = 0
        symbols_input = 0
        for i in range(password_length):
            what_char_is = choice([1,2,3])
            if what_char_is == 1:
                char_input += 1
            elif what_char_is == 2:
                numbers_input += 1
            else:
                symbols_input += 1
        generated_password = random_password(pass_length=password_length,letters_qt=char_input,numbers_qt=numbers_input,symbols_qt=symbols_input)
        print("Your new password is: ", generated_password)
        break
    elif pass_option == "2":
        password_length = int(input("Enter the password length: "))
        char_input = int(input("How many letters would you like your password to have? :"))
        numbers_input = int(input("How many numbers would you like your password to have?: "))
        symbols_input = int(input("How many symbols would you like your password to have?: "))
        if password_length != sum([char_input, numbers_input, symbols_input]):
            print("Password length does not match. Try again.")
        else:
            generated_password = random_password(pass_length=password_length, letters_qt=char_input, symbols_qt=symbols_input , numbers_qt=numbers_input )
            print(f"Your new password is: {generated_password}")
            break
    elif pass_option == "quit":
        break
    else:
        print("Invalid choice. Please try again or type 'quit'.")
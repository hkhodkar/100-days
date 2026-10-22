import art;
import alphabet;

print(art.logo);

close_session = False;


def main(text, shifted_number, encrypt = True):
    cipher_text = "";
    for char in text.lower():
        alphabet_index = alphabet.alphabet.index(char);
        if encrypt:
            shifted_index = alphabet_index + int(shifted_number);
        else:
            shifted_index = alphabet_index - int(shifted_number);
        shifted_index %= len(alphabet.alphabet);
        cipher_text += alphabet.alphabet[shifted_index]
    if encrypt:
        print(f"here is encoded result: {cipher_text} \n") 
    else:
        print(f"here is decoded result: {cipher_text} \n") 
    
    
while not close_session:
    text = input("Type your message \n")
    shifted = input("Type the shift number \n")
    main(text,shifted);

    coded_text = input("Type your encrypted message \n")
    coded_shifted = input("Type the shift number \n")
    main(coded_text,coded_shifted, False)
    
    is_session_closed = input("Reset session? type 'y' for yes and 'n' for no \n")
    if  is_session_closed  !='y' or not is_session_closed  != 'n':
        input("Invalid answer! type 'y' for yes and 'n' for no \n")
    if is_session_closed == 'n':
        close_session = True;
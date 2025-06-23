# credit_card_app/encryption_utils.py
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

SECRET_KEY = b'GSqTMBuptm_1ObiT8ITc32C4hQ4zuern'

def encrypt_credit_card(credit_card):
    cipher = Cipher(algorithms.AES(SECRET_KEY), modes.CFB(b'\0' * 16), backend=default_backend())
    encryptor = cipher.encryptor()

    encrypted_credit_card = encryptor.update(credit_card.encode('utf-8'))
    encoded_data = base64.urlsafe_b64encode(encrypted_credit_card)

    print("Encrypted Credit Card:", encoded_data.decode('utf-8'))

    return encoded_data.decode('utf-8')

def decrypt_credit_card(encrypted_credit_card):
    try:
        decoded_data = base64.urlsafe_b64decode(encrypted_credit_card)
    except base64.binascii.Error as e:
        return {'error': f'Invalid base64-encoded string: {str(e)}'}

    try:
        cipher = Cipher(algorithms.AES(SECRET_KEY), modes.CFB(b'\0' * 16), backend=default_backend())
        decryptor = cipher.decryptor()

        decrypted_credit_card = decryptor.update(decoded_data) + decryptor.finalize()

        # Print encrypted and decrypted values for debugging
        print("Decrypted Credit Card:", decrypted_credit_card)

        # Do not decode the decrypted_credit_card, as it is already in bytes
        return {'data': decrypted_credit_card}
    except Exception as e:
        return {'error': str(e)}

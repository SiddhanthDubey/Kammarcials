from app import app


class Encryption:
    def __init__(self, key):
        self.key = key

    def encrypt(self, data):
        encrypted_data = ""
        for char in data:
            encrypted_data += chr(ord(char) + self.key)
        app.logger.debug("Encryption: {} -> {}".format(data, encrypted_data))
        return encrypted_data


class Decryption:
    def __init__(self, key):
        self.key = key

    def decrypt(self, encrypted_data):
        decrypted_data = ""
        for char in encrypted_data:
            decrypted_data += chr(ord(char) - self.key)
        app.logger.debug("Decryption: {} -> {}".format(encrypted_data, decrypted_data))
        return decrypted_data

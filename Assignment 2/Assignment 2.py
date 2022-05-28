import rsa


publicKey, privateKey = rsa.newkeys(512)

# this is the string that we will be encrypting
message = input("Please type your secret message: ")

encMessage = rsa.encrypt(message.encode(),publicKey)

print("Original message: ", message)
print("Encrypted message: ", encMessage)


decMessage = rsa.decrypt(encMessage, privateKey).decode()

print("Decrypted Message: ", decMessage)

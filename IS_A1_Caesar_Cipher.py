"""
SIMPLE CAESAR CIPHER
This program shifts letters to encrypt messages
Example: "HELLO" with shift 3 becomes "KHOOR"
"""

def caesar_encrypt(text, shift):
    """
    STEP BY STEP:
    1. Take each letter from text
    2. If it's a letter, shift it
    3. If not a letter, keep it as is
    4. Return the new text
    """
    
    new_text = ""
    
    # Look at each character one by one
    for character in text:
        
        # Check if it's a letter
        if character.isalpha():
            
            # Handle uppercase letters (A-Z)
            if character.isupper():
                old_position = ord(character) - 65
                new_position = (old_position + shift) % 26
                new_character = chr(new_position + 65)
            
            # Handle lowercase letters (a-z)
            else:
                old_position = ord(character) - 97
                new_position = (old_position + shift) % 26
                new_character = chr(new_position + 97)
            
            # Add shifted character
            new_text += new_character
        
        else:
            # Keep spaces and special characters unchanged
            new_text += character
    
    return new_text


def caesar_decrypt(ciphertext, shift):
    """
    To decrypt, shift backwards
    """
    return caesar_encrypt(ciphertext, -shift)


# ====================================
# Testing the program
# ====================================

print("=" * 50)
print("SIMPLE CAESAR CIPHER")
print("=" * 50)

# Get message from user
user_message = input("\nEnter your message: ")

# Get shift from user
user_shift = int(input("Enter shift number (1-25): "))

# Make sure shift is within range
user_shift = user_shift % 26

# Encrypt the message
encrypted_message = caesar_encrypt(user_message, user_shift)

# Show results
print("\n" + "-" * 30)
print("RESULTS:")
print("-" * 30)
print(f"Original:  {user_message}")
print(f"Encrypted: {encrypted_message}")

# Decrypt to verify
decrypted_message = caesar_decrypt(encrypted_message, user_shift)
print(f"Decrypted: {decrypted_message}")

# Check if it worked
if user_message == decrypted_message:
    print("\n✓ Success! The message was properly encrypted and decrypted.")
else:
    print("\n✗ Something went wrong.")

# Show example
print("\n" + "-" * 30)
print("HOW IT WORKS:")
print("-" * 30)
print("A → B → C → D ... (shift 1)")
print("HELLO → KHOOR (shift 3)")
print("Only letters change, spaces stay the same")
from PIL import Image
import hashlib
import random
import string

def generate_complex_password_from_image(image_path, length=16):
    try:
        # Open the image file
        img = Image.open(image_path)
        # Convert the image to a consistent format (e.g., RGB)
        img = img.convert('RGB')
        # Get the image data as a byte array
        img_bytes = img.tobytes()
        # Generate a SHA-256 hash from the byte data
        password_hash = hashlib.sha256(img_bytes).hexdigest()
        
        # Add complexity: include uppercase, symbols, and numbers
        # Create a character pool with letters, digits, and symbols
        char_pool = string.ascii_letters + string.digits + string.punctuation
        
        # Randomize the hash and map it to the character pool
        random.seed(password_hash)  # Use the hash to seed the randomness
        complex_password = ''.join(random.choices(char_pool, k=length))
        
        return complex_password
    except Exception as e:
        return f"Error: {e}"

# Example Usage
if __name__ == "__main__":
    image_path = input("Enter the path to your image file: ")
    password_length = int(input("Enter the desired password length (default 16): ") or 16)
    password = generate_complex_password_from_image(image_path, password_length)
    print(f"Generated Complex Password: {password}")

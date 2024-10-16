import base64
import binascii
import urllib.parse
from codecs import decode

def print_watermark():
    print("##############")
    print("MADE BY GRIFFIN")
    print("##############\n")

def is_base64(s):
    try:
        # Base64 harus memiliki panjang kelipatan 4
        if len(s) % 4 == 0:
            base64.b64decode(s)
            return True
    except Exception:
        return False
    return False

def is_hex(s):
    try:
        bytes.fromhex(s)
        return True
    except ValueError:
        return False

def is_url_encoded(s):
    try:
        decoded = urllib.parse.unquote(s)
        if decoded != s:
            return True
    except Exception:
        return False
    return False

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def is_utf8(s):
    try:
        s.encode('utf-8')
        return True
    except UnicodeEncodeError:
        return False

def is_base32(s):
    try:
        if len(s) % 8 == 0:
            base64.b32decode(s)
            return True
    except Exception:
        return False

def is_base58(s):
    base58_alphabet = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
    return all(c in base58_alphabet for c in s)

def is_rot13(s):
    try:
        decoded = decode(s, 'rot_13')
        if decoded != s:
            return True
    except Exception:
        return False

def detect_encoding(s):
    print_watermark()
    
    if is_hex(s):
        print("Detected encoding: Hexadecimal")
        try:
            print(f"Decoded value: {bytes.fromhex(s).decode('utf-8')}")
        except UnicodeDecodeError:
            print("Error: Unable to decode hex as UTF-8, possibly binary data.")
    elif is_base64(s):
        print("Detected encoding: Base64")
        try:
            print(f"Decoded value: {base64.b64decode(s).decode('utf-8')}")
        except UnicodeDecodeError:
            print("Error: Unable to decode Base64 as UTF-8, possibly binary data.")
    elif is_url_encoded(s):
        print("Detected encoding: URL Encoding")
        print(f"Decoded value: {urllib.parse.unquote(s)}")
    elif is_ascii(s):
        print("Detected encoding: ASCII")
        print(f"Decoded value: {s}")
    elif is_utf8(s):
        print("Detected encoding: UTF-8")
        print(f"Decoded value: {s}")
    elif is_base32(s):
        print("Detected encoding: Base32")
        try:
            print(f"Decoded value: {base64.b32decode(s).decode('utf-8')}")
        except UnicodeDecodeError:
            print("Error: Unable to decode Base32 as UTF-8, possibly binary data.")
    elif is_base58(s):
        print("Detected encoding: Base58")
        # Base58 decoding is not implemented here, as it requires custom libraries
        print("Decoding requires a special library (e.g., Bitcoin libraries)")
    elif is_rot13(s):
        print("Detected encoding: ROT13")
        print(f"Decoded value: {decode(s, 'rot_13')}")
    else:
        print("Encoding type is not recognized!")

input_str = input("Enter text encoding: ")
detect_encoding(input_str)

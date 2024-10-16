# encode-and-decode-system
1. User Input:
A. The system asks the user to enter text that is suspected to be a certain encoding.
B. The input will be processed by the detect_encoding function.

2. Encoding Type Detection:
A. After receiving input, the system sequentially checks whether the text conforms to one of the following encoding methods: Hexadecimal, Base64, URL Encoding, ASCII, UTF-8, Base32, Base58, and ROT13.
B. For each method, the system uses a special function that verifies whether the text conforms to the encoding rules.

How This System Works in General:
A. The system tries to detect an encoding that matches the given input.
B. When an encoding is detected, the system decodes the input if possible and displays the result.
C. If the input cannot be decoded to UTF-8 (e.g. binary data), the system displays a relevant error message.
D. If no encoding matches, the system informs that the encoding type is not recognized.

This system works sequentially to detect the type of encoding using special functions, then provides decoding results. Error handling is done to ensure that invalid data does not cause the system to crash.

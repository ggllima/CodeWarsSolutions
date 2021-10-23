# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

# If the function is passed a valid PIN string, return true, else return false.

# Examples (Input --> Output)
# "1234"   -->  true
# "12345"  -->  false
# "a234"   -->  false

def validate_pin(pin):
    import re
    if re.findall("[a-zA-Z,.,+,:,#,\-,/,\n, ]",pin) or len(pin) != 4 and len(pin) != 6 or type(pin) != str:
        return False
    return True
import base64
import string
import random

#  A new custom charset
#  Change this guy to desired string. Append the "=" char if you also want to possibly change its location.
cuscharset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

#  The standard charset
#  If you added an "=" char, or some other char to cuscharst above, make sure to add it here as well.
b64charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

encodedset = string.maketrans(b64charset, cuscharset)
decodedset = string.maketrans(cuscharset, b64charset)


def dataencode(x):
    y = base64.b64encode(x)
    y = y.translate(encodedset)
    return y


def datadecode(x):
    y = x.translate(decodedset)
    y = base64.b64decode(y)
    return y


def randset():
    """Generate a random alphabet for use in base64 encoding"""
    x = "".join(random.sample(cuscharset, len(cuscharset)))
    global encodedset
    global decodedset
    encodedset = string.maketrans(b64charset, x)
    decodedset = string.maketrans(x, b64charset)
    if len(cuscharset) == 64:
        print "New random charset: " + x + "="
    elif len(cuscharset) == 65:
        print "New random charset: " + x

    print "Record the above string if you ever want to be able to decode this data again.\n"

# Uncomment the command below to generate a random base64 alphabet.
#randset()

plaintext = "Some string to be base64 encoded."

#  Encode the plaintext string
enc = dataencode(plaintext)
#  Decode back into plaintext string
dec = datadecode(enc)

print enc
print dec
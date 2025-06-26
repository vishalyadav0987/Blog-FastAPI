# --------------------------------------------------------------
#  passlib.context se CryptContext import karte hain
#  -------------------------------------------------------------
#  🔹 Passlib ek popular Python library hai jo secure password
#     hashing algorithms (bcrypt, argon2, pbkdf2, … ) ko easy
#     wrapper deti hai. CryptContext un algorithms ko manage
#     karne-ka “settings object” hai.
from passlib.context import CryptContext


# --------------------------------------------------------------
#  CryptContext ka ek instance bana rahe hain
#  -------------------------------------------------------------
#  🔹 schemes=['bcrypt']
#        → Sirf bcrypt algorithm ko allow karo.  bcrypt modern,
#          salt-based, adaptive hashing hai – brute-force se bachata hai.
#  🔹 deprecated='auto'
#        → Agar future me multiple schemes list hon aur unme se
#          koi outdated ho jaye to Passlib usse “deprecated” mark kare.
#          Yaha single bcrypt hai, to effect zero – but future-ready hai.
pwd_cxt = CryptContext(
    schemes=['bcrypt'],
    deprecated='auto'
)


# --------------------------------------------------------------
#  Helper class: Hash
#  -------------------------------------------------------------
#  Iska purpose sirf ek jaga par “hash password” ka logic rakhna
#  hai taaki baar-baar CryptContext import na karna pade.
class Hash:

    # ----------------------------------------------------------
    #  Static method bcrypt(password: str) → str
    #  ---------------------------------------------------------
    #  🔹 StaticMethod decorator lagana optional hai, lekin good
    #    practice: method ko 'self' ki zarurat nahī̃, kyunki
    #    bas ek utility function hai.
    #  🔹 Type hint `password: str` batata hai ki yeh plain-text
    #    password string expect karta hai.
    #  🔹 Return value Passlib-generated hash string hoti hai,
    #    jisme algorithm identifier + salt + cost factor sab
    #    embed hota hai (e.g. "$2b$12$eImiTXuWVxfM37uY4JANjQ…").
    @staticmethod
    def bcrypt(password: str):
        # pwd_cxt.hash() → internally:
        #    • random salt generate karta hai
        #    • bcrypt algorithm se hash banata hai
        #    • final string return karta hai
        return pwd_cxt.hash(password)
    
    def verify(userPassword,password):
        return pwd_cxt.verify(userPassword,password)

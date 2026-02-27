from quickpass import create_password

password = create_password(length=32, include_symbols=True)
print("password generated:", password)

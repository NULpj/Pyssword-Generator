import argparse
import random
import string
import secrets
import pyperclip

# ==== ARGPARSE ====
parser = argparse.ArgumentParser(description="Advanced Pyssword Generator")

# Basic
parser.add_argument("-l", "--length", type=int, default=12, help="Password length")
parser.add_argument("-n", "--number", type=int, default=1, help="Number of passwords to generate")
parser.add_argument("-d", "--digits", action="store_true", help="Include digits")
parser.add_argument("-sy", "--symbols", action="store_true", help="Include symbols (!@#$%%^&*)")
parser.add_argument("-a", "--no-ambiguous", action="store_true", help="Avoid ambiguous characters like 'O', '0', 'I', 'l'")
parser.add_argument("-sv", "--save", metavar="file.txt", help="Save output to file")
parser.add_argument("-c", "--copy", action="store_true", help="Copy the first password to clipboard")

# Advanced
parser.add_argument("-u", "--uppercase", action="store_true", help="Include uppercase letters (A-Z)")
parser.add_argument("-lo", "--lowercase", action="store_true", help="Include lowercase letters (a-z)")
parser.add_argument("-x", "--exclude", metavar="CHARS", help="Exclude specific characters (e.g., 01lIO)")
parser.add_argument("-p", "--prefix", metavar="STR", help="Add a prefix to each password")
parser.add_argument("-suf", "--suffix", metavar="STR", help="Add a suffix to each password")
parser.add_argument("-nd", "--no-duplicate", action="store_true", help="No duplicate characters allowed")
parser.add_argument("-sd", "--seed", type=int, help="Use specific seed for reproducible randomness")
parser.add_argument("-sec", "--secure", action="store_true", help="Enable all security options (digits, symbols, letters, no-ambiguous)")
parser.add_argument("-v", "--verbose", action="store_true", help="Show detailed info while running")
parser.add_argument("-V", "--version", action="version", version="Pyssword-Gen v1.0.0", help="Show version")

args = parser.parse_args()

# ==== PASSWORD RATING ====
def rate_password(pw):
    score = 0
    length = len(pw)

    if length >= 8:
        score += 1
    if length >= 12:
        score += 1
    if length >= 16:
        score += 1

    if any(c.islower() for c in pw):
        score += 1
    if any(c.isupper() for c in pw):
        score += 1
    if any(c.isdigit() for c in pw):
        score += 1
    if any(c in "!@#$%^&*()-_=+[]{}|;:<>,.?/~`" for c in pw):
        score += 1

    if len(set(pw)) == len(pw):  # all characters unique
        score += 1

    if any(c in "O0Il1" for c in pw):
        score -= 1  # penalty for ambiguous characters

    if score <= 3:
        return "Weak"
    elif score <= 5:
        return "Medium"
    elif score <= 7:
        return "Strong"
    else:
        return "Very Strong"

# ==== BUILD CHARACTER SET ====
char_set = ""

if args.secure:
    args.uppercase = args.lowercase = args.digits = args.symbols = args.no_ambiguous = True

if args.uppercase:
    char_set += string.ascii_uppercase
if args.lowercase:
    char_set += string.ascii_lowercase
if args.digits:
    char_set += string.digits
if args.symbols:
    char_set += "!@#$%^&*()-_=+[]{}|;:<>,.?/~`"

# Default minimal fallback
if not char_set:
    char_set = string.ascii_letters + string.digits

# Remove ambiguous characters
if args.no_ambiguous:
    for ch in "0OIl1":
        char_set = char_set.replace(ch, "")

# Exclude specific characters
if args.exclude:
    for ch in args.exclude:
        char_set = char_set.replace(ch, "")

if args.seed is not None:
    random.seed(args.seed)

# ==== GENERATE PASSWORDS ====
passwords = []

for _ in range(args.number):
    if args.no_duplicate and args.length > len(set(char_set)):
        raise ValueError("Password length exceeds the number of unique available characters without duplicates.")

    if args.no_duplicate:
        chars = random.sample(char_set, args.length)
    else:
        chars = [secrets.choice(char_set) for _ in range(args.length)]

    password = ''.join(chars)

    if args.prefix:
        password = args.prefix + password
    if args.suffix:
        password = password + args.suffix

    passwords.append(password)

# ==== OUTPUT ====
for i, pw in enumerate(passwords):
    rating = rate_password(pw)
    print(f"[{i+1}] {pw}  ({rating})")

if args.copy and passwords:
    pyperclip.copy(passwords[0])
    print("\n📋 First password copied to clipboard.")

if args.save:
    with open(args.save, 'w') as f:
        for pw in passwords:
            rating = rate_password(pw)
            f.write(f"{pw} ({rating})\n")
    print(f"\n💾 Passwords saved to file: {args.save}")

if args.verbose:
    print("\n[INFO]")
    print(f"Password length          : {args.length}")
    print(f"Number of passwords      : {args.number}")
    print(f"Include digits           : {args.digits}")
    print(f"Include symbols          : {args.symbols}")
    print(f"Include uppercase letters: {args.uppercase}")
    print(f"Include lowercase letters: {args.lowercase}")
    print(f"Avoid ambiguous chars    : {args.no_ambiguous}")
    print(f"No duplicate characters  : {args.no_duplicate}")
    print(f"Excluded characters      : {args.exclude}")
    print(f"Prefix                   : {args.prefix}")
    print(f"Suffix                   : {args.suffix}")
    print(f"Seed                     : {args.seed}")

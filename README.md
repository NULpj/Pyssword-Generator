# 🔐 Advanced Pyssword Generator

A highly customizable, secure, and command-line-based password generator built with Python.

This tool allows users to generate one or multiple passwords with full control over character sets, length, duplication, ambiguity, and even clipboard/csv output. Ideal for developers, sysadmins, or anyone who needs strong passwords on demand.

---

## 🚀 Features

- Generate one or more passwords at once
- Specify:
  - Length
  - Digits, symbols, lowercase, uppercase
  - Prefix/suffix
  - No duplicate characters
  - Avoid ambiguous characters (like `0`, `O`, `I`, `l`)
- Password rating: Weak, Medium, Strong, Very Strong
- Clipboard support (auto-copy first password)
- Save to file
- Reproducible generation using a seed
- Verbose output for detailed control
- Secure random generator (`secrets` module)

---

## 📦 Requirements

Only one external dependency is required:

```
pyperclip
```

Install it using:

```bash
pip install -r requirements.txt
```

---

## 📄 Usage

```bash
python main.py [options]
```

### 🔧 Examples

```bash
# Generate a single strong password of 16 characters
python main.py -l 16 -d -sy -u -lo

# Generate 5 passwords with no ambiguous characters and copy the first one
python main.py -n 5 -l 12 -a -c -d -sy -u -lo

# Save 10 passwords to passwords.txt
python main.py -n 10 -l 20 -sy -d -u -lo -sv passwords.txt

# Verbose output
python main.py -l 16 -sec -v
```

---

### ⚙️ Command-Line Options

| Short Flag | Long Flag         | Description                                                                  |
|------------|-------------------|------------------------------------------------------------------------------|
| `-l`       | `--length`        | Password length (default: 12)                                                |
| `-n`       | `--number`        | Number of passwords to generate                                              |
| `-d`       | `--digits`        | Include digits                                                               |
| `-sy`      | `--symbols`       | Include symbols (!@#$%^&*)                                                   |
| `-u`       | `--uppercase`     | Include uppercase letters (A–Z)                                              |
| `-lo`      | `--lowercase`     | Include lowercase letters (a–z)                                              |
| `-a`       | `--no-ambiguous`  | Avoid ambiguous characters (`0`, `O`, `I`, `l`)                              |
| `-x`       | `--exclude`       | Exclude specific characters                                                  |
| `-p`       | `--prefix`        | Add a prefix to each password                                                |
| `-suf`     | `--suffix`        | Add a suffix to each password                                                |
| `-nd`      | `--no-duplicate`  | Disallow duplicate characters                                                |
| `-sd`      | `--seed`          | Use specific random seed (for reproducible generation)                       |
| `-sec`     | `--secure`        | Enable all secure options (digits, symbols, uppercase/lowercase, no-ambig)   |
| `-c`       | `--copy`          | Copy the first generated password to clipboard                               |
| `-sv`      | `--save`          | Save all generated passwords to a file                                       |
| `-v`       | `--verbose`       | Show detailed configuration info during execution                            |
| `-V`       | `--version`       | Show version info and exit                                                   |

---

### 📊 Password Rating System

Each generated password is rated to help you evaluate its strength. The score is based on:

- ✅ Password length
- ✅ Presence of lowercase letters
- ✅ Presence of uppercase letters
- ✅ Presence of digits
- ✅ Presence of symbols
- ✅ Unique characters (no repetition)
- ❌ Penalty if it contains ambiguous characters (`0`, `O`, `I`, `l`)

**Rating Categories:**

| Score Range | Rating        |
|-------------|---------------|
| 0–3         | 🔴 Weak        |
| 4–5         | 🟠 Medium      |
| 6–7         | 🟢 Strong      |
| 8+          | 💪 Very Strong |

---

## 📁 File Structure

```
Pyssword-Generator/
├── main.py
├── requirements.txt
├── README.md
```

---

## 📜 License

This project is licensed under the MIT License.  
Feel free to use, modify, and distribute.

---

## 🙌 Credits

Built with ❤️ using Python and `secrets`, `pyperclip`.

Author: NULpj

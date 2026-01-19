# pingu-translator 🐧

Stop saying human language... let's **noot noot**!

Pingu Translator is a fun Python library and CLI tool that lets you:

- Encode any Unicode text into **Pingu language** (`noot`, `nooooot`, etc.)
- Decode Pingu back into human-readable text
- Optionally compress long messages for efficiency
- Keep your secret messages "noot-ified" 🕵️‍♂️

---

## Features

- ✅ Supports **any Unicode text**: ASCII, Chinese, emojis, and more
- ✅ Fixed-length encoding ensures **reversible transformation**
- ✅ Automatic **compression for long text**
- ✅ Fun CLI tool for quick encoding/decoding
- ✅ Customizable **Pingu tokens** with carrier letters (`n`, `o`, `t`) and invisible variation selectors

---

## Installation

```bash
git clone https://github.com/<your-username>/pingu-translator.git
cd pingu-translator
pip install -e .
```

## Usage

### Python

```python
from encoding import encoder, decoder

text = "Hello, 世界! 😀"
pingu_text = encoder.encode(text)
print(repr(pingu_text))  # Use repr() to see invisible characters

decoded = decoder.decode(pingu_text)
print(decoded)  # "Hello, 世界! 😀"
```

> **Tip:** Pingu text may contain invisible Unicode variation selectors. Always use `repr()` or write to a file to inspect it safely.

### CLI

```bash
# Encode text
python pingu_cli.py encode "Hello, 世界!"

# Decode Pingu text
python pingu_cli.py decode "<pingu_text_here>"
```

## Notes

- Short text (<12 bytes) is encoded as-is; long text is compressed automatically
- Designed to be **reversible**: encoding → decoding always returns the original text

## Contributing

Want to add more fun features? Feel free to submit PRs or open issues!

Let's make the world a **nootier place**. 🐧

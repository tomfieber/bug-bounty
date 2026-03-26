# JavaScript Deobfuscation

Techniques and tools for deobfuscating JavaScript code encountered during security testing.

## Commands

Hex encode

```bash
echo plaintext | xxd -p
```

Hex decode

```bash
echo ENCODED_HEX | xxd -p -r
```

Rot13 encode

```bash
echo plaintext | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```

Rot13 decode

```bash
echo ENCODED_ROT13 | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```

# Deobfuscation Websites

| **Website**                                     |
| ----------------------------------------------- |
| [JS Console](https://jsconsole.com/)            |
| [Prettier](https://prettier.io/playground/)     |
| [Beautifier](https://beautifier.io/)            |
| [JSNice](http://www.jsnice.org/)                |
| [Unpacker](https://matthewfl.com/unPacker.html) |

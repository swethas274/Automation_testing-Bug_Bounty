# 🔐 Cookie & JWT Manipulation Tool (Authorized Testing)

## 📌 Overview

This tool is a **command-line utility for authorized security testing** that helps analyze, modify, and re-encode **Base64-encoded cookies containing JWT access tokens**.

It is designed to assist in testing **authentication and authorization logic** in web applications **with explicit permission**, using **test accounts only**.

---

## 🧠 What the Tool Does

The tool performs a **full decode → modify → re-encode workflow** on cookies that follow this structure:


### Core Capabilities

- ✅ Decodes **Base64-encoded cookies** into readable JSON
- ✅ Automatically decodes **JWT access tokens** (header + payload)
- ✅ Extracts **all parameters**, including nested fields
- ✅ Displays parameters in an interactive table
- ✅ Allows the user to choose one or more parameters to modify
- ✅ Copies values between two test-user cookies
- ✅ Re-encodes:
  - JWT (when applicable)
  - Entire cookie back to Base64
- ✅ Saves:
  - Original decoded cookies
  - Modified decoded cookies
  - Final Base64-encoded cookie for testing

---

## 🔄 Typical Workflow

1. Provide **two Base64-encoded cookies** (from two test users)
2. Tool decodes both cookies and their JWT access tokens
3. All parameters (including nested ones) are displayed in a readable table
4. User selects a parameter to modify (e.g. `user.email`, `access_token.payload.sub`)
5. Value from Cookie B is copied into Cookie A
6. Cookie A is safely re-encoded:
   - JWT → string
   - JSON → Base64
7. Output is saved for reuse in tools like **Burp Suite**

---

## 📂 Output Files

For each execution, the tool creates JSON files:

```
user_1.json
user_1(1).json
user_2.json
```

### Modified cookie

The modified file contains:

```json
{
  "decoded_cookie": {
    "...": "Readable decoded cookie data"
  },
  "cookie_encoded": "BASE64_ENCODED_COOKIE_STRING"
}
```

## Intended Use Cases

1. Authorization testing (IDOR, broken access control)

2. JWT trust and claim validation

3. Detecting mismatches:
- user.id vs access_token.payload.sub
- user.email vs JWT email

4. Session handling verification

5. Manual testing using Burp Suite or curl

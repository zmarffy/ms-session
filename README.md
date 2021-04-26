# `ms-login`

`ms-login` is a tiny Python library that provides a way to log in to your Microsoft account programatically in a `requests` `Session`. It is widely unknown why you would ever want to use this, but that's for you to determine.

## Usage

The usage is incredibly simple and straightforward. Just create a new `MSSession` object and pass it your creds.

```python
from ms_login import MSSession

session = MSSession("someone@example.com", "password")
```

The returned object is a subclass of `requests.Session` and has you logged in to your Microsoft account.

```python
"someone@example.com" in session.get("https://account.microsoft.com/")  # True
```

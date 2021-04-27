# `ms-session`

`ms-session` is a tiny Python library that provides a way to log in to your Microsoft account programatically in a `requests` `Session`. It is widely unknown why you would ever want to use this, but that's for you to determine. I just make the library.

## Usage

The usage is incredibly simple and straightforward. Just create a new `MSSession` object and pass it your creds.

```python
from ms_session import MSSession

session = MSSession("someone@example.com", "password")
```

The returned object is a subclass of `requests.Session` and has you logged in to your Microsoft account.

```python
"someone@example.com" in session.get("https://account.microsoft.com/")  # True
```

## Known issues

- Rarely (it seems to occur for Microsoft accounts that have not been logged into for a very long time), a required key may be missing from an API response that is required to be passed to the next. This will prevent you from logging in using `ms-session`. There may be a way further traverse the chain of requests needed to log in, but I have found that logging in to that account manually once seems to get it back in shape to be used with `ms-session`. If you figure anything out about combatting this, feel free to submit a PR
- Accounts protected by two-factor auth are not supported, and I have no plans to do so ever

## Special thanks

A huge thank you to [@Terrance](https://github.com/Terrance) and his [SkPy](https://github.com/Terrance/SkPy) library. He and his library were able to point me in the correct direction for understadning how tricky values such as `t` work.

The Chromium Dev Tools are your best friend when it comes to reversing services. Do not sleep on them.

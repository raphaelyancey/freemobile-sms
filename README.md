# freemobile-sms 💻

Command-line program to send a SMS with the [Free Mobile](https://mobile.free.fr) API.
Should work with Python2 and Python3 thanks to `future`.

## Install

```
$ pip install future
$ git clone https://github.com/raphaelyancey/freemobile-sms.git
$ cd freemobile-sms
$ chmod +x freemobile-sms.py
$ mv freemobile-sms.py /usr/local/bin/freemobile-sms
```

## Usage

```
$ freemobile-sms -u [user ID] -k [API key] -m "Hello world!"
# or: freemobile-sms --user [user ID] --key [API key] --message "Hello world!"
```

## Troubleshooting

```
Traceback (most recent call last):
  File "/usr/local/bin/freemobile-sms", line 34, in <module>
    from future.builtins import *
ImportError: No module named future.builtins
```

You installed `future` with the wrong `pip`: install `future` accordingly with the `pip` that matches the `python -V` version (like `pip2` if `python -V` is 2.x).

## TODO

- Reading from a `~/.freemobile` configuration file
- Package for PyPi and easy installation with `pip install freemobile-sms`

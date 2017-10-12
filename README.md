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

## TODO

- Reading from a `~/.freemobile` configuration file
- Package for PyPi and easy installation with `pip install freemobile-sms`

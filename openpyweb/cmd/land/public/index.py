#!/usr/local/bin/python
try:
    from openpyweb import Web

except Exception as err:
    exit(err)

App = Web.App()
App.runs()

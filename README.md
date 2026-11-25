# Acme Licensing API

Acme Licensing API is a Django project for managing software licenses and trials.
The idea is to give staff a central place to manage licenses, ease support and error detection.
The app will be hybrid type - containing backend web UI and REST API for clients (licensed programs).
REST API will let client applications check whether a license or trial is still valid.

## Products
Products are company's commercial apps, that allow try before buy option.
Each app has its own unique code, combination of one letter + two digits.

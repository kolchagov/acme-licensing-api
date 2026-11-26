# Acme Licensing API

Acme Licensing API is a Django project for managing software licenses and trials.
The idea is to give staff a central place to manage licenses, ease support and error detection.
The app will be hybrid type - containing backend web UI and REST API for clients (licensed programs).
REST API will let client applications check whether a license or trial is still valid.

## Idea explanation and workflow

Acme company has several software applications (products), that embrace the try before buy license principle.
Also while the company grow, a several distributor companies become partners.
This project helps manage trial periods and licensing to company customers.

### Prerequisites:

1. Backend users need to be created by admin. They can be either company staff or distributor companies.
 If user is a company, company name becomes mandatory, if distributor is willing to receive payments IBAN needs
 to be set. Optionally the companies can have logo (shown in the list)

2. The products (apps) need to be created with all required fields (name, code, version)

### How trial and licensing works:

1. A company product (app or bundle) has its own unique code, composed of one letter and two digits: A01

- Installer app makes POST to backend endpoint by sending its host device serail number and app code. this
 action starts trial period for device
- A device can have multiple apps in different trial stages
- Each trial record compose a unique licensing key, composed of joined app code (converted to 4 digits)
 and trial record PK (padded with 0 to 4 digits). To that base is appended Luhn check digit to avoid typin or
 spelling errors.

2. Once customer liked the app and proceed to purchase, the distributor or staff creates a customer record with its
 data.

- After payment, Customer gives its trial code and the user license the app by using this code.

## Products

Products are company's commercial apps, that allow try before buy option.
Each app has its own unique code, combination of one letter + two digits. Products can be bundled in packages with
several apps and discounted price (many-to-many relation).

## Customers

Model contain standard fields, with unique fields: UIC (unique identifier code) and unique VAT number.
Customer can own many products (many-to-many relation)

## Exception logs

The apps can upload exceptions in the company's backed, using POST API requests.
These records can be analyzed by staff and ticketed to fix the found errors.

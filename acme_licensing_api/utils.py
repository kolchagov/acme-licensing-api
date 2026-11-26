def convert_code(code):
    """
    convert code to digits. Letter A is 11
    :param code: app code, e.g. A01, already cleaned by Django
    :return: converted 4 digits string: 1101
    """
    # if not re.match(r'^[A-L]\d\d$',code):
    #     raise ValueError("Invalid code")
    prefix = 10 + (ord(code[0]) - ord('A') + 1)
    return f'{prefix}{code[1:]}'


def luhn_checksum(base):
    """Return the Luhn check digit for base, ready to append to it."""
    def digits_of(n):
        return [int(digit) for digit in str(n)]

    digits = digits_of(base)
    # the check digit will follow base, so base's last digit gets doubled
    doubled_digits = digits[-1::-2]
    other_digits = digits[-2::-2]
    checksum = sum(other_digits)
    for d in doubled_digits:
        checksum += sum(digits_of(d * 2))
    return (10 - checksum % 10) % 10


def is_luhn_valid(check_number):
    check_number = str(check_number)
    return luhn_checksum(check_number[:-1]) == int(check_number[-1])


def trial_code_generator(trial) -> str:
    base = convert_code(trial.app.code) + f"{trial.pk:04}"
    return base + str(luhn_checksum(base))

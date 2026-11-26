from trials.models import Trial


def convert_code(code):
    """
    convert code to digits. Letter A is 11
    :param code: app code, eg. A01, already cleaned by Django
    :return: converted 4 digits string: 1101
    """
    # if not re.match(r'^[A-L]\d\d$',code):
    #     raise ValueError("Invalid code")
    prefix = 10 + (ord(code[0]) - ord('A') + 1)
    return f'{prefix}{code[1:]}'


def luhn_checksum(base):
    def digits_of(n):
        return [int(d) for d in str(n)]

    digits = digits_of(base)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d * 2))
    return checksum % 10


def is_luhn_valid(check_number):
    return luhn_checksum(check_number) == 0


def trial_code_generator(trial: Trial) -> str:
    base = convert_code(trial.code) + f"{trial.pk:5}"
    return base + str(luhn_checksum(base))

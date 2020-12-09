import string


def validate_doc_rule_1(doc, req_fields):
    if len(doc) < len(req_fields):
        return False

    for field in req_fields:
        if field not in doc:
            return False

    return True


def validate_int(doc, field, min_val, max_val):
    if field not in doc:
        return False

    val = int(doc[field])
    return min_val <= val <= max_val


def validate_byr(doc):
    return validate_int(doc, 'byr', 1920, 2002)


def validate_iyr(doc):
    return validate_int(doc, 'iyr', 2010, 2020)


def validate_eyr(doc):
    return validate_int(doc, 'eyr', 2020, 2030)


def validate_hgt(doc):
    if 'hgt' not in doc:
        return False

    hgt = doc['hgt']

    if len(hgt) < 4:
        return False

    val = hgt[0:-2]
    unit = hgt[-2:]

    if unit == 'in':
        return 59 <= int(val) <= 76
    elif unit == 'cm':
        return 150 <= int(val) <= 193

    return False


def validate_hcl(doc):
    if 'hcl' not in doc:
        return False

    val = doc['hcl']

    if len(val) != 7:
        return False

    # string.hexdigits new feature in python 3.8
    return all(c in string.hexdigits for c in val[-6:])


def validate_ecl(doc):
    if 'ecl' not in doc:
        return False

    return doc['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def validate_pid(doc):
    if 'pid' not in doc:
        return False
    
    return len(doc['pid']) == 9 and int(doc['pid']) > 0


def validate_doc_rule_2(doc):
    return validate_byr(doc) \
        and validate_iyr(doc) \
        and validate_eyr(doc) \
        and validate_hgt(doc) \
        and validate_hcl(doc) \
        and validate_ecl(doc) \
        and validate_pid(doc) 


def part_1():
    # Read input into an array of passport parameter lists.
    input_file = open("resources/input04.txt")
    # Items are separated by a blank row.
    my_input = [a.split() for a in input_file.read().strip().split('\n\n')]
    input_file.close()
    docs = []

    # Convert each item into a dictionary to facilitate future lookups by key.
    for doc in my_input:
        docs.append(dict([field.split(':') for field in doc]))

    valid_count = 0

    for doc in docs:
        if validate_doc_rule_1(doc, ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']):
            valid_count += 1

    return valid_count


def part_2():
    # Read input into an array of passport parameter lists.
    input_file = open("resources/input04.txt")
    # Items are separated by a blank row.
    my_input = [a.split() for a in input_file.read().strip().split('\n\n')]
    input_file.close()
    docs = []

    # Convert each item into a dictionary to facilitate future lookups by key.
    for doc in my_input:
        docs.append(dict([field.split(':') for field in doc]))

    valid_count = 0

    for doc in docs:
        if validate_doc_rule_2(doc):
            valid_count += 1

    return valid_count


def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()

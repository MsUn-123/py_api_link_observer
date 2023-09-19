import shlex

def validate_input_add(input):
    if len(input) == 3: return True
    else: return False

def validate_input_remove(input):
    if len(input) == 1 and input[0].isnumeric(): return True
    else: return False 

def validate_input_test(input):
    if len(input) == 2: return True
    else: return False

def extract_arg(arg):
    return shlex.split(arg)[1:]

def parse_response_list(input):
    output = input[1:]
    output = output[:-1]
    return output

def clear_escapes(input):
    if "\n" in input:
        input = input.replace(' ','').replace('\n', '')
    return input
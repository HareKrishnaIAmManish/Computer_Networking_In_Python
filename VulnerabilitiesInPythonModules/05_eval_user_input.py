import re
python_code=input()
pattern=re.compile(r'valid_input_regular_expressions')
if pattern.fullmatch(python_code):
    eval(python_code)
    

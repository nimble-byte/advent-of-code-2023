import re
from os import path

sum = 0

inputPath = path.join(path.dirname(__file__), 'input.txt')

def replace_digits(reg_match):
  digit = reg_match.group()
  print(f'  {digit}')
  match digit:
    case 'one':
      return '1'
    case 'two':
      return '2'
    case 'three':
      return '3'
    case 'four':
      return '4'
    case 'five':
      return '5'
    case 'six':
      return '6'
    case 'seven':
      return '7'
    case 'eight':
      return '8'
    case 'nine':
      return '9'

file = open(inputPath, 'r')
lines = file.read().splitlines()

for line in lines[:10]:
  print(line)
  line = re.sub(r'one|two|three|four|five|six|seven|eight|nine', replace_digits, line)
  print(f'  {line}')
  # strip characters
  digits = re.sub(r'[a-z]+', '', line)
  # print(f'  {digits}')
  # digits = re.findall(r'\d', line)

  first = int(digits[0])
  last = int(digits[-1])

  # print(f'    first: {first}')
  # print(f'    last: {last}')
  sum += 10 * first + last

print(sum)

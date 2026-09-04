# เขียนโปรแรมตรวจสอบความแข็งเเรงของ PASSWORD
# นิยาม strong password คือ ยาวมากกว่า 8 ตัว,มีอักขระ @1 ตัว,ตัวเลข,มีตัวอักษร

#Insert You password : xxxxx
#You password is strong!

#Insert You password : @xxxxx
#You password is strong!

test_str =input('password')
print(f"\nValidation methods for '{test_str}':")
print(f"isalnum(): {test_str.isalnum()}")
print(f"isalpha(): {test_str.isalpha()}")
print(f"isdigit(): {test_str.isdigit()}")
print(f"isupper(): {test_str.isupper()}")
print(f"islower(): {test_str.islower()}")

password = "hdegd1"
lenght =len(password)
words = password.split('@')  

if len(words) >1 and password.count('@')== 1:
 left = words[0].isalnum
 right = words[1].isalnum   
else:
    left = False
    right = False 
if lenght >=8 and len(words) == 2 and left and right:
    print("You password is strong")
else:
    print("You password is not strong")

print("\n=== ORD() AND CHR() FUNCTIONS ===")
ch = 'R'
print(f"ord('{ch}') = {ord(ch)}")
print(f"chr(82) = {chr(82)}")

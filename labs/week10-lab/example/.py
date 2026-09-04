# 1.รับค่า text จากผู้ใช้
# 2.รับค่าอักขระที่ต้องการค้นหาจากผู้ใช้
# 3.แสดงผลจำนวนของอักขระในข้อความ text

# Insert you Text : Boonchoo Jitunpong
# Charactor to find : o
# 5 Letters 'o' found 'in Boonchoo Jitunpong'

print("\n=== ITERATING THROUGH STRING ===")
count = 0
text = input("name :")
char = input("Charater :")
for letter in text:
    if letter == char:
        count += 1
print(f"{count} letters 'o' found in '{text}'")

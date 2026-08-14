# เขียน function แปลงหน่วยสกุลเงิน ที่สามารถแปลง
#THB <-> USD ..1 USD =32 THB 
#THB <-> JYP ..100 JYP =22 THB
#โดยใช้ชื่อและการใช้งาน 
# function convert_currency(100,"USD) 
#แสดงผลออกทางหน้าจอ
#100 THB = 3.3 USD
#และทดสอบ function ที่ตัวเองเขียนด้วย


def convert_currency(a,b):
    if b == "USD":
        print(f"{a}THB = {a /32.0},USD")
    else :
       print(a,"USD = ",a * 32.0,"THB") 

convert_currency(100,"USD")
convert_currency(100,"THB")


def calculate_triangle_area(Hight, base):
    """Calculates and displays triangle area"""
    area = Hight * base
    print(f"Triangle with Hight {Hight} and base {base}")
    print(f"Area = 0.5 * {Hight} × {base} = {area}")
    print()
 
print("Calculating rectangle areas:")
calculate_triangle_area(5, 3)
calculate_triangle_area(10, 7)
 
 
# เขียน function แปลงหน่วยสกุลเงิน ที่สามารถแปลง
#THB <-> USD ..1 USD =32 THB 
#THB <-> JYP ..100 JYP =22 THB

#โดยใช้ชื่อและการใช้งาน 
# function convert_currency(100,"USD) 

#แสดงผลออกทางหน้าจอ
#100 THB = 3.3 USD
#และทดสอบ function ที่ตัวเองเขียนด้วย
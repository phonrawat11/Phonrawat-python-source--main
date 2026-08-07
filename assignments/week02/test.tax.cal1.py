print("Tax calculator")
print("progressive Tax Rate")
print("0-150,000 = 0%")
print("151,000-300,000 = 5%")
print("300,001-500,000 = 10%")
print("500,001-750,000= 15%")
print("750,001-1,000,000 = 20%")
print("1,000,001-2,000,000 = 25%")
print("2,000,001-5,000,000 = 30%")
print(">5,000,000 = 35%")
Tax = 0
monney = float(input("Amount: "))

if 0 <= monney <= 150000:
    print("Duty free")
    ptint("Tax=0%")

elif 150000 > monney <= 300000:
    Tax = (monney - 150000) * 0.05
    total = monney - Tax
    print("Tax:", Tax)
    print("total:", total)
    ptint("Tax=5%")

elif monney > 300000 and monney < 500000 :
    tax_1_percent = (300000 - 150000) * 0.05 
    tax_2_percent = (monney - 300000) * 0.10
  
    Tax = tax_1_percent + tax_2_percent
    total = monney - Tax
    print("Tax:", Tax)
    print("total:", total)
    ptint("Tax=10%")
    
elif monney > 500000 and monney < 750000 :
    tax_3_percent = 27500
    tax_4_percent = (monney - 500000) * 0.15
    
    Tax = tax_3_percent + tax_4_percent
    total = monney - Tax
    print("Tax:", Tax)
    print("total:", total)
    ptint("Tax=15%")
    
elif monney > 750000 and monney < 1000000 :
    tax_5_percent = 65000
    tax_6_percent = (monney - 750000) * 0.20
    
    Tax = tax_5_percent + tax_6_percent
    total = monney - Tax
    print("Tax:", Tax)
    print("total:", total) 
    ptint("Tax=20%")
    
elif monney > 1000000 and monney < 2000000 :
    tax_7_percent = 115000
    tax_8_percent = (monney - 1000000) * 0.25
    
    Tax = tax_7_percent + tax_8_percent
    total = monney - Tax
    print("Tax:", Tax)
    print("total:", total) 
    ptint("Tax=25%")   
    
elif monney > 2000000 and monney < 5000000 :
    tax_9_percent = 365000
    tax_10_percent = (monney - 2000000) * 0.30
    
    Tax = tax_9_percent + tax_10_percent
    total = monney - Tax
    print("Tax:", Tax)
    print("total:", total)
    ptint("Tax=30%")  
    
elif monney > 5000000 :
    tax_11_percent = 1265000
    tax_12_percent = (monney - 5000000) * 0.35
    
    Tax = tax_11_percent + tax_12_percent
    total = monney - Tax
    print("Tax:", Tax)
    print("total:", total)  
    ptint("Tax=35%")  
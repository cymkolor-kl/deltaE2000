# 導入所需模塊 
import math
import cms
def delta_e_2000(lab1, lab2):

# 定義ΔE 2000計算公式函數

    L1, a1, b1 = lab1
    L2, a2, b2 = lab2

    avg_Lp = (L1 + L2) / 2
    C1 = math.sqrt(a1**2 + b1**2)
    C2 = math.sqrt(a2**2 + b2**2)
    avg_C1_C2 = (C1 + C2) / 2

    G = (1 - math.sqrt(avg_C1_C2 ** 7 / (avg_C1_C2 ** 7 + 25 ** 7))) / 2

    a1_prime = a1 * (1 + G)
    a2_prime = a2 * (1 + G)

    C1_prime = math.sqrt(a1_prime**2 + b1**2)
    C2_prime = math.sqrt(a2_prime**2 + b2**2)
    avg_C1_C2_prime = (C1_prime + C2_prime) / 2

    avg_a1_a2_prime = (a1_prime + a2_prime) / 2
    avg_b1_b2 = (b1 + b2) / 2

    delta_L_prime = L2 - L1
    delta_C_prime = C2_prime - C1_prime
    delta_a_prime = a2_prime - a1_prime
    delta_b_prime = b2 - b1

    S_L = 1
    S_C = 1 + 0.045 * avg_C1_C2_prime
    S_h = 1 + 0.015 * avg_C1_C2_prime * math.sqrt(avg_a1_a2_prime**2 + avg_b1_b2**2)

    delta_E = math.sqrt( (delta_L_prime / S_L) ** 2
                    + (delta_C_prime / S_C) ** 2  
                    + (delta_a_prime / S_h) ** 2
                    + (delta_b_prime / S_h) ** 2 )

    return delta_E

# 呼叫函數計算兩組Lab顏色的ΔE 2000
	
# lab1 = (50, 20, -30)
# lab2 = (48, 22, -32) 

print("請輸入第一個Lab颜色值,以空格分隔:")  
lab1 = input().split(' ')
lab1 = [float(x) for x in lab1] 

print("請輸入第二個Lab颜色值,以空格分隔:")
lab2 = input().split(' ') 
lab2 = [float(x) for x in lab2]

delta_e = delta_e_2000(lab1, lab2)
print('%.2f' % delta_e) #四捨五入到小數點以下兩位
input("按任意鍵繼續...")
# print(delta_e)
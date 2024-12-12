string = "กระต่ายหลงตัวเอง ชอบโอ้อวดว่าวิ่งเร็วกว่าใครๆ เมื่อเห็นเต่าเดินต้วมเตี้ยมมาก็หัวเราะเยาะ พร้อมกับพูดจาถากถางว่าต่อให้เต่าวิ่งนำหน้าไปก่อน กระต่ายก็สามารถก็แซงหน้าได้อยู่ดี ทำให้เต่าเกิดความไม่พอใจ จึงท้ากระต่ายวิ่งแข่งกัน กระต่ายเริ่มวิ่งนำหน้าเต่าไปไกล แต่เมื่อไปถึงครึ่งทาง ก็เกิดความชะล่าใจ หยุดพักเอนกายนอนใต้ต้นไม้ใหญ่จนเผลอหลับไป ในขณะที่เต่ายังคงเดินต่อไปเรื่อยๆ อย่างไม่ลดละ เมื่อกระต่ายตื่นนอนขึ้นมาก็ตกใจ รีบลนลานวิ่งไปยังเส้นชัย ทว่าเต่าไปถึงเส้นชัยก่อนแล้ว"
thai_ch = "กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤฤๅลฦฦๅวศษสหฬอฮ"
new_string = string.replace(" ", "")

count_ch = 0
list_ch = []
dict_ch = {}
new_dict_ch = {}

for ch in new_string:
    if ch in thai_ch:
        count_ch += 1
        if ch not in dict_ch:
            dict_ch[ch] = 1
        else:
            dict_ch[ch] += 1

list_ch = list(sorted(dict_ch.keys()))
new_dict_ch = dict(sorted(dict_ch.items()))

print(f"count of consonant {count_ch}")
print(f"list of consonant {list_ch}")
print(f"dict of consonant {new_dict_ch}")

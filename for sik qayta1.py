# ruyxat=['ali','vali','salim','qudrat','bektemur']

# for i in ruyxat:
#     print("assalomu alaykum "+i.title())
#     print("bbugun kechki 7 da futbolga kelasizmi?")
# print("takrorlanishlar soni: ",len(ruyxat))    
# numbrs=list(range(11,100,2))
# for num in numbrs:
#     print(f"{num} ning kubi {num**3}")

# films=list(range(5))
# kinolar=[]
# for i in films:
#     kinolar.append(input(f"{i+1}- film nomini kiriting.\n>>"))
# print(kinolar)

yaqinlar=[]
suhbatlashish=int(input("bugun necha kishi bilan suhbatlashdingiz? >>>"))
for i in range(suhbatlashish):
    yaqinlar.append(input(f"{i+1}- suhbat qurgan insonning ismi: "))
print(yaqinlar)


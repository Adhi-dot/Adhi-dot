class pemain_ea_fc_mobile :
    def __init__(self, nama, ovr, posisi, tipe, program, training_level, gold):
        self.nama = nama
        self.ovr = ovr
        self.posisi = posisi
        self.tipe = tipe
        self.program = program
        self.training_level = training_level
        self.gold = gold

    def level_training(self):
        if self.training_level < 30:
            self.training_level += 1
            print (f"{self.nama} naik ke training level {self.training_level}")
        else :
            print (f"{self.nama} mencapai training level maksimal")
    
    def RUP (self):
        if self.ovr <122:
            self.ovr +=  1
            print (f"{self.nama} naik ke ovr {self.ovr}")
        else :
            print (f"{self.nama} mencapai ovr maksimal")

gold_balance = 7829000000 #7 milyar 829 juta

def sold_player(player, gold_balance):
    tax = 0.1
    sales_result = player.gold - (player.gold * tax)
    curent_gold_balance = gold_balance + sales_result

    print ("\nTransfer Market")
    print (f"Player {player.nama} sold {sales_result}")
    print (f"tax 10%:{int(player.gold * tax):,}")
    return curent_gold_balance

class Striker(pemain_ea_fc_mobile):
    def __init__(self, nama, ovr, posisi, tipe, program, training_level, gold):
        super().__init__(nama, ovr, posisi, tipe, program, training_level, gold)
        self.traits = "Finesse Shot, Power Header, Speed Dribbler, driven free kick, leadership"

    def Poacher (self):
        print (f"{self.nama} memiliki kemampuan {self.traits} untuk menciptakan goal")

def sold_player(player, gold_balance):
    tax = 0.05
    sales_result = player.gold - (player.gold * tax)
    curent_gold_balance = gold_balance + sales_result

    print ("\nTransfer Market")
    print (f"Player {player.nama} sold {sales_result}")
    print (f"tax 5%:{int(player.gold * tax):,}")
    return curent_gold_balance

print("\n")
p1 = Striker ("Pele", 122, "striker", "False 9", "Icon capped legends", 30, 6293400000)
p1.level_training()
p1.Poacher()
p2 = Striker ("Fernando Torres", 120, "striker", "Poacher", "Glorious eras icon signature", 30, 6293400000)
p2.level_training()
p2.Poacher()

gold_balance = sold_player(p1, gold_balance)
gold_balance = sold_player(p2, gold_balance)

print ("\n")
print (f"Pemain : {p1.nama}")
print (f"OVR: {p1.ovr} | Posisi: {p1.posisi} | Tipe: {p1.tipe}")
print (f"Harga pasar : {p1.gold:,} gold")
print (f"Traits : {p1.traits}")

print ("\n")
print (f"Pemain : {p2.nama}")
print (f"OVR: {p2.ovr} | Posisi: {p2.posisi} | Tipe: {p2.tipe}")
print (f"Harga pasar : {p2.gold:,} gold")
print (f"Traits : {p2.traits}")

print ("\n" + "="*30)
print (f"Current gold balance :{int(gold_balance):,}")
print ("=" *30)
class Hero:
    def __init__(self,name,hp):
        self.name = name
        self.hp = hp
    def take_damage(self,amount):
        self.amount = amount
        self.hp -= self.amount
        print(self.name,"is at",self.hp,"hp, they took",self.amount,"damage")
Arthur = Hero("Arthur",20)
Arthur.take_damage(10)
Morgana = Hero("Morgana",20)
Morgana.take_damage(0)

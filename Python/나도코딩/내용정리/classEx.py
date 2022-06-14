class Unit:
    # 생성자 __init__
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp


# Unit을 상속
class AttackUnit(Unit):
    # 생성자 __init__
    def __init__(self, name, hp, damage):
        # 상속 생성자
        Unit.__init__(self, name, hp)
        self.damage = damage
        print(name, hp, damage)

    # self는 자기 자신으로 맨 앞에 무조건 적어준다고 생각하면 됨.
    # self. 이 아니면 전달받은
    def attack(self, location):
        print(self.name, location, self.damage)


class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed


# 2개 이상 상속도 가능
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)


marine1 = Unit("marine", 40, 5)
marine2 = Unit("marine", 40, 5)
tank = Unit("tank", 150, 35)

# 변수 추가 할당 가능(해당 인스턴스에만 가능)
tank.clocking = True
print(tank.clocking)
print(tank)

# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # 아무것도 안하고 일단 넘어간다.
        pass
        # super를 함께 쓸 경우 self를 사용하면 안됨.
        super().__init__(name, hp, 0)
        self.location = location


supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")


def game_over():
    pass


# 아무것도 실행이 안됨.
game_over()

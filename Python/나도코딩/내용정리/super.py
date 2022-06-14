# 메소드 오버라이딩은 패스(자바랑 너무 같음)

# super


class Unit:
    def __init__(self):
        print("Unit 생성자")


class Flyable:
    def __init__(self):
        print("Flyable 생성자")


class FlyableUnit(Unit, Flyable):
    def __init__(self):
        # 2개 이상 상속받을 경우 먼저 선언한 부모클래스 생성자만 호출(super로 할 경우) -> 모든 생성자 호출이 필요할 경우 각각 init호출해줘야 함.
        super().__init__()
        Flyable.__init__(self)


example = FlyableUnit()

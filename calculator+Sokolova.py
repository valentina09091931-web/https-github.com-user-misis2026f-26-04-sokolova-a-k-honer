class BodyMassIndex:
    def __init__(self, weight, height):
        self.weight=weight
        self.height=height
    def value(self):
        height_m=self.height/100
        return self.weight/(height_m**2)
    def category(self):
        bmi=self.value()
        if bmi<16:
            return 'выраженный дефицит массы'
        elif bmi<18.5:
            return 'недостаточная масса'
        elif bmi<25:
            return 'норма'
        elif bmi<30:
            return 'предожирение'
        elif bmi<35:
            return 'ожирение 1 степени'
        elif bmi<40:
            return 'ожирение 2 степени'
        else:
            return 'ожирение 3 степени'
    def healthy_weight(self):
        heigth_m=self.height/100
        low=18.5*heigth_m**2
        high=24.9*heigth_m**2
        return round(low, 1), round(high,1)
    def report(self):
        low, high=self.healthy_weight()
        print('вес:', self.weight, 'кг')
        print('рост', self.height, 'см')
        print('имт', round(self.value(),2))
        print('категория', self.category())
        print('нормальные параметры', low, '-', high, 'кг')
while True:
    weight=float(input('введите свой вес, кг'))
    height=float(input('введите свой рост, см'))
    bmi=BodyMassIndex(weight, height)
    bmi.report()
    

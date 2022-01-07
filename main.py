class Car:
    def __init__(self,speed=0):
        self.speed = speed
        self.odometer = 0
        self.time = 0

    def say_state(self):
        print("I am going{}kph!".format(self.speed))

    def accelerate(self):
        self.speed += 5

    def brake(self):
        if self.speed < 5:
            self.speed = 0
        else:
            self.speed -= 5

    def step(self):
        self.odometer += self.speed
        self.time += 1

    def avarage_speed(self):
        if self.time != 0:
            return self.odometer / self.time
        else:
            pass

if __name__ =='__main__':
    my_car = Car()
    print("I am a car!")
    while True:
        action = input("What should I do?[A]ccelerate, [B]rake, show[O]dometer, or show avarage[S]peed").upper()
        if action not in "ABOS" or len(action) != 1:
            print("I do not know that")
            continue
        if action == 'A':
            my_car.accelerate()
        elif action =='B':
            my_car.brake()
        elif action == 'O':
            print("The car has been driven {} kilometers".format(my_car.odometer))
        elif action == 'S':
            print("The car has an avarage speed was {} kph".format(my_car.avarage_speed()))
        my_car.step()
        my_car.say_state()



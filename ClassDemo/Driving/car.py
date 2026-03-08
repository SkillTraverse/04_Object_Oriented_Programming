class Engine:
    def __init__(self):
        self.running = False

    def start(self):
        self.running = True
        print("Engine started")

    def stop(self):
        self.running = False
        print("Engine stopped")

class Throttle:
    def accelerate(self, car):
        if car.engine.running:
            car.speed += 10
            print(f"Accelerating. Speed: {car.speed} km/h")
        else:
            print("Cannot accelerate. Engine is off.")

class Brake:
    def apply(self, car):
        car.speed = max(0, car.speed - 10)
        print(f"Braking. Speed: {car.speed} km/h")

class Steering:
    def turn_left(self):
        print("Turning left")

    def turn_right(self):
        print("Turning right")

class Nitro:
    def boost(self, car):
        if car.engine.running:
            car.speed += 30
            print(f"Nitro boost! Speed: {car.speed} km/h")
        else:
            print("Engine must be running to use nitro")

class Car:
    def __init__(self):
        self.speed = 0

        self.engine = Engine()
        self.throttle = Throttle()
        self.brake = Brake()
        self.steering = Steering()
        self.nitro = Nitro()

car = Car()

car.engine.start()

car.throttle.accelerate(car)
car.throttle.accelerate(car)

car.steering.turn_left()

car.nitro.boost(car)

car.brake.apply(car)
car.brake.apply(car)

car.engine.stop()
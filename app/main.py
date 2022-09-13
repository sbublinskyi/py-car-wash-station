class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str
    ):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int
    ):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list):
        price = 0
        for car in cars:
            price += self.wash_single_car(car)
        return price

    def calculate_washing_price(self, car: Car):
        total = car.comfort_class * (self.clean_power - car.clean_mark)
        return round(
            total * self.average_rating / self.distance_from_city_center, 1
        )

    def wash_single_car(self, car: Car):
        if car.clean_mark > self.clean_power:
            return 0

        price = self.calculate_washing_price(car)
        car.clean_mark = self.clean_power
        return price

    def rate_service(self, rate: int):
        count = self.average_rating * self.count_of_ratings + rate
        self.average_rating = round(count / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1

#8.12 Make a sandwich
def make_sandwich(*items):
    print("I'm making a sandwich with these ingredients:")
    for item in items:
        print(f"- {item}")
    print("Enjoy your sandwich!\n")


make_sandwich("ham", "cheese", "lettuce")
make_sandwich("turkey", "tomato")
make_sandwich("peanut butter", "jelly", "banana", "honey")


#8.13 build my profile
def build_profile(first, last, **user_info):
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info

my_profile = build_profile("Rafa", "Ogirima",
                          age=40,
                          course="mathematics",
                          location="ilorin" )

print(my_profile)


#8.14 make a car
def make_car(type, manufacturer, **car_info):
    car_info["car type"] = type
    car_info["manufacturer"] = manufacturer
    return car_info


car = make_car("electric", "Volkswagen", 
               model=2010, 
               color="white" )

print(car)
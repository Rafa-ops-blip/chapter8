#8.3 T-shirt
def make_shirt(shirt_size, message):
  print(f"\nMake me an {shirt_size.upper()} shirt and {message.upper()} should be boldly written on it.")


make_shirt('xxl', 'high fashion')
make_shirt(shirt_size='l', message='main g')


#8.4 Large Shirts with default size
def make_shirt(message, shirt_size='l'):
  print(f"\nMake me an {shirt_size.upper()} shirt and {message.title()} should be boldly written on it.")


make_shirt(message='i love python')


#8.4 medium shirt with default message
def make_shirt(shirt_size, message='i love python'):
  print(f"\nMake me an {shirt_size.upper()} shirt and {message.title()} should be boldly written on it.")


make_shirt(shirt_size='m')
make_shirt(shirt_size='xl', message='this is bliss!')


#8.5 Cities
def describe_city(city_name, country='China'):
  print(f"\n{city_name.title()} is a very beautiful city in {country.title()}")


describe_city('chongqing')
describe_city(city_name='beijing')
describe_city(country='canada', city_name='toronto')

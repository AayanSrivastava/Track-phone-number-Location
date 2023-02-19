import phonenumbers
from numbers_dataset import number
from phonenumbers import geocoder
chnum=phonenumbers.parse(number,"CH") #C- for country H- for history
print(geocoder.description_for_number(chnum,"en"))

# for Service provider information

from phonenumbers import carrier
service_provider = phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_provider,"en"))
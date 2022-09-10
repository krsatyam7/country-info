# importing the module
from countryinfo import CountryInfo

# taking country name as input
count= input("Enter your country : ")

# passing input in countryinfo module
country= CountryInfo(count)

# printing the capital of the country
print("\nCapital is :",country.capital())

# printing the currency of the country
print("\nCurrencies is :",country.currencies())

# printing the languages used in country
print("\nLanguage is :",country.languages())

# printing names of other country sharing its border with the Country.
print("\nBorders are :",country.borders())

# printing alternative names of country
print("\nOther names :",country.alt_spellings())

# printing the area of the country
print("\nArea is :",country.area(),"Km²")

# printing the population of the country
print("\nPopulation is :",country.population())

# printing the calling code of the country
print("\nCalling code is :",country.calling_codes())

# printing the timezone of the country
print("\nTimezone is :",country.timezones())

# printing the Native name of the country
print("\nNative name is :",country.native_name())

# printing the Provinces of the country
print("\nProvinces are :",country.provinces())


# printing the wikipedia link of the country
print("\nWikipedia Link :",country.wiki())
      

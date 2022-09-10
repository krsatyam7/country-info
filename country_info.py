# importing the module
from countryinfo import CountryInfo

# taking country name as input
count= input("Enter your country : ")

# passing input in countryinfo module
country= CountryInfo(count)

# printing the capital of the country
print("\n\033[1mCapital is :\033[0m",country.capital())

# printing the currency of the country
print("\n\033[1mCurrencies is :\033[0m",country.currencies())

# printing the languages used in country
print("\n\033[1mLanguage is :\033[0m",country.languages())

# printing names of other country sharing its border with the Country.
print("\n\033[1mBorders are :\033[0m",country.borders())

# printing alternative names of country
print("\n\033[1mOther names :\033[0m",country.alt_spellings())

# printing the area of the country
print("\n\033[1mArea is :\033[0m",country.area(),"Km²")

# printing the population of the country
print("\n\033[1mPopulation code is :\033[0m",country.population())

# printing the calling code of the country
print("\n\033[1mCalling code is :\033[0m",country.calling_codes())

# printing the timezone of the country
print("\n\033[1mTimezone is :\033[0m",country.timezones())

# printing the Native name of the country
print("\n\033[1mNative name is :\033[0m",country.native_name())

# printing the Provinces of the country
print("\n\033[1mProvinces are :\033[0m",country.provinces())


# printing the wikipedia link of the country
print("\n\033[1mWikipedia Link :\033[0m",country.wiki())
      
      
# used print("\033[1m xxxxxx \033[0m") to print text in bold format.
# just replace xxxxxx with your desired word to print the text.

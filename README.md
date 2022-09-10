# country-info
A python module for returning data about countries, ISO info and states/provinces within them.

**Run this code online by clicking this** [link](https://colab.research.google.com/drive/16OJTXF9CK5qIv4r2B72dIMpVMF52FQj9)
1. Run [cell 1](https://colab.research.google.com/drive/16OJTXF9CK5qIv4r2B72dIMpVMF52FQj9#scrollTo=EE3DjNH42xHa)
2. Then run [cell 2](https://colab.research.google.com/drive/16OJTXF9CK5qIv4r2B72dIMpVMF52FQj9#scrollTo=bEGMwcaY270U)
3. Give country name as and input and you are done.
# Python Module used 
* [countryinfo](https://pypi.org/project/countryinfo/)
 *  Module used in this repo belong to their respective owners and I or this repo does not claim any right over them.
 
 **********************************
 
<b> Note : </b> File "country_info.py" will not run on basic python idle, due to some limitations (unable to print bold characters).
           use another file "country_info1.py" to run it in basic idles

## Table of Contents

* [Install](#install)
* [API Usage](#api-usage)

## APIs
* [.info()](#info)
* [.provinces()](#provinces)
* [.alt_spellings()](#alt_spellings)
* [.area()](#area)
* [.borders()](#borders)
* [.calling_codes()](#calling_codes)
* [.capital()](#capital)
* [.capital_latlng()](#capital_latlng)
* [.currencies()](#currencies)
* [.demonym()](#demonym)
* [.geojson()`](#geo_json)
* [.iso()](#iso)
* [.languages()](#languages)
* [.latlng()](#latlng)
* [.native_name()](#native_name)
* [.population()](#population)
* [.region()](#region)
* [.subregion()](#subregion)
* [.timezones()](#timezones)
* [.tld()](#tld)
* [.translations()](#translations)
* [.wiki()](#wiki)
* [.google()](#google)
* [.all()](#all)


## Install

```python
pip install countryinfo
```

OR, git clone

```python
git clone https://github.com/porimol/countryinfo.git

cd countryinfo
python setup.py install
```

## API Usage
To access one of the country properties available, you'll need to use one of the API methods listed below and pass a country in either way.

### .info()

Returns all available information for a specified country.

```python
# coding=utf-8
from countryinfo import CountryInfo


country = CountryInfo('Singapore')
country.info()
# returns object,
{
    'ISO': {
        'alpha2': 'SG',
        'alpha3': 'SGP'
    },
    'altSpellings': [
        'SG',
        'Singapura',
        'Republik Singapura',
        '新加坡共和国'
    ],
    'area': 710,
    'borders': [],
    'callingCodes': ['65'],
    'capital': 'Singapore',
    'capital_latlng': [
        1.357107,
        103.819499
    ],
    'currencies': ['SGD'],
    'demonym': 'Singaporean',
    'flag': '',
    'geoJSON': {},
    'languages': [
        'en',
        'ms',
        'ta',
        'zh'
    ],
    'latlng': [
        1.36666666,
        103.8
    ],
    'name': 'Singapore',
    'nativeName': 'Singapore',
    'population': 5469700,
    'provinces': ['Singapore'],
    'region': 'Asia',
    'subregion': 'South-Eastern Asia',
    'timezones': ['UTC+08:00'],
    'tld': ['.sg'],
    'translations': {
        'de': 'Singapur',
        'es': 'Singapur',
        'fr': 'Singapour',
        'it': 'Singapore',
        'ja': 'シンガポール'
    },
    'wiki': 'http://en.wikipedia.org/wiki/singapore',
    'google': 'https://www.google.com/search?q=Singapore'
}

# Similar can also be achieved via country code or any
# alternate name of a country. For example, Singapur
# would be:
country = CountryInfo('SG')
```

### .provinces()
Return provinces list

```python
# coding=utf-8
from countryinfo import CountryInfo


country = CountryInfo('Singapore')
country.provinces()
# returns object,
['Singapore']
```

### .alt_spellings()

Returns alternate spellings for the name of a specified country

```python
# coding=utf-8
from countryinfo import CountryInfo


country = CountryInfo('Singapore')
country.alt_spellings()
# returns list of strings, alternate names
# ['SG', 'Singapura', 'Republik Singapura', '新加坡共和国']
```

### .area()

Returns area (km²) for a specified country

```python
# coding=utf-8
from countryinfo import CountryInfo


country = CountryInfo('Singapore')
country.area()
# returns number of square kilometer area
710
```

### .borders()

Returns bordering countries (ISO3) for a specified country

```python
# coding=utf-8
from countryinfo import CountryInfo


country = CountryInfo('Singapore')
country.borders()
# returns array of strings, ISO3 codes of countries that border the given country
[]
```

### .calling_codes()

Returns international calling codes for a specified country

```python
# coding=utf-8
from countryinfo import CountryInfo


country = CountryInfo('Singapore')
country.calling_codes()
# returns array of calling code strings
['65']
```

### .capital()

Returns capital city for a specified country

```python
# coding=utf-8
from countryinfo import CountryInfo


country = CountryInfo('Singapore')
country.capital()
# returns string
'Singapore'
```

### .capital_latlng()

Returns capital city latitude and longitude for a specified country

```python
# coding=utf-8
from countryinfo import CountryInfo


country = CountryInfo('Singapore')
country.capital_latlng()
# returns array, approx latitude and longitude for country capital
[1.357107, 103.819499]
```

### .currencies()

Returns official currencies for a specified country

```python
# coding=utf-8
from countryinfo import CountryInfo


country = CountryInfo('Singapore')
country.currencies()
# returns array of strings, currencies
# ['SGD']
```

### .demonym()

Returns the [demonyms](http://en.wikipedia.org/wiki/Demonym) for a specified country

```python
# coding=utf-8
from countryinfo import CountryInfo


country = CountryInfo('Singapore')
country.demonym()
# returns string, name of residents
'Singaporean'
```

### .geo_json()

Returns [geoJSON](http://en.wikipedia.org/wiki/GeoJSON) for a specified country

```python
# coding=utf-8
from countryinfo import CountryInfo


country = CountryInfo('Bangladesh')
country.geo_json()
# returns object of GeoJSON data

{
    'features': [
        {
            'geometry': {
                'coordinates': [[[92.672721, 22.041239],
                                             [92.652257, 21.324048],
                                             [92.303234, 21.475485],
                                             [92.368554, 20.670883],
                                             [92.082886, 21.192195],
                                             [92.025215, 21.70157],
                                             [91.834891, 22.182936],
                                             [91.417087, 22.765019],
                                             [90.496006, 22.805017],
                                             [90.586957, 22.392794],
                                             [90.272971, 21.836368],
                                             [89.847467, 22.039146],
                                             [89.70205, 21.857116],
                                             [89.418863, 21.966179],
                                             [89.031961, 22.055708],
                                             [88.876312, 22.879146],
                                             [88.52977, 23.631142],
                                             [88.69994, 24.233715],
                                             [88.084422, 24.501657],
                                             [88.306373, 24.866079],
                                             [88.931554, 25.238692],
                                             [88.209789, 25.768066],
                                             [88.563049, 26.446526],
                                             [89.355094, 26.014407],
                                             [89.832481, 25.965082],
                                             [89.920693, 25.26975],
                                             [90.872211, 25.132601],
                                             [91.799596, 25.147432],
                                             [92.376202, 24.976693],
                                             [91.915093, 24.130414],
                                             [91.46773, 24.072639],
                                             [91.158963, 23.503527],
                                             [91.706475, 22.985264],
                                             [91.869928, 23.624346],
                                             [92.146035, 23.627499],
                                             [92.672721, 22.041239]]],
                            'type': 'Polygon'
                },
               'id': 'BGD',
               'properties': {'name': 'Bangladesh'},
               'type': 'Feature'}],
    'type': 'FeatureCollection'
}

```

### .iso()

Returns ISO codes for a specified country

```python
# coding=utf-8
from countryinfo import CountryInfo


country = CountryInfo('Singapore')
country.iso()
# returns object of ISO codes
{'alpha2': 'SG', 'alpha3': 'SGP'}

country.iso(2)
# returns object of ISO codes
'SG'


country.iso(3)
# returns object of ISO codes
'SGP'
```

### .languages()

Returns official languages for a specified country

```python
# coding=utf-8
from countryinfo import CountryInfo


country = CountryInfo('Singapore')
country.languages()
# returns array of language codes
['en', 'ms', 'ta', 'zh']
```

### .latlng()

Returns approx latitude and longitude for a specified country

```python
# coding=utf-8
from countryinfo import CountryInfo


country = CountryInfo('Singapore')
country.latlng()
# returns array, approx latitude and longitude for country
[1.36666666, 103.8]
```

### .native_name()

Returns the name of the country in its native tongue

```python
# coding=utf-8
from countryinfo import CountryInfo


country = CountryInfo('Singapore')
country.native_name()
# returns string, name of country in native language
'Singapore'
```

### .population()

Returns approximate population for a specified country

```python
# coding=utf-8
from countryinfo import CountryInfo


country = CountryInfo('Singapore')
country.population()
# returns number, approx population
5469700
```

### .region()

Returns general region for a specified country

```python
# coding=utf-8
from countryinfo import CountryInfo


country = CountryInfo('Singapore')
country.region()
# returns string
'Asia'
```

### .subregion()

Returns a more specific region for a specified country

```python
# coding=utf-8
from countryinfo import CountryInfo


country = CountryInfo('Singapore')
country.subregion()
# returns string
'South-Eastern Asia'
```

### .timezones()

Returns all timezones for a specified country

```python
# coding=utf-8
from countryinfo import CountryInfo


country = CountryInfo('Singapore')
country.timezones()
# returns array of timezones
['UTC+08:00']
```

### .tld()

Returns official [top level domains](http://en.wikipedia.org/wiki/Top-level_domain) for a specified country

```python
# coding=utf-8
from countryinfo import CountryInfo


country = CountryInfo('Singapore')
country.tld()
# returns array of top level domains specific to the country
['.sg']
```

### .translations()

Returns translations for a specified country name in popular languages

```python
# coding=utf-8
from countryinfo import CountryInfo


country = CountryInfo('Singapore')
country.translations()
# returns object of translations of country name in major languages
{
    'de': 'Singapur',
    'es': 'Singapur',
    'fr': 'Singapour',
    'it': 'Singapore',
    'ja': 'シンガポール'
}
```

### .wiki()

Returns link to wikipedia page for a specified country

```python
# coding=utf-8
from countryinfo import CountryInfo


country = CountryInfo('Singapore')
country.wiki()
# returns string URL of wikipedia article on country
'http://en.wikipedia.org/wiki/singapore'
```

### .google()

Returns link to google page for a specified country

```python
# coding=utf-8
from countryinfo import CountryInfo


country = CountryInfo('Singapore')
country.google()
# returns string URL of google page on country
'https://www.google.com/search?q=Singapore'
```


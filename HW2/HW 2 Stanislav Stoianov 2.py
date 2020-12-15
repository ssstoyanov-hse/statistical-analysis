countries = {};

while not len(countries) == 10:
    countryName = input(u"Введите название страны: ");
    capitalName = countries.get(countryName);
    if capitalName is None:
        countries[countryName] = input(u"Введите название столицы: ");
    else:
        print(f"Столица {countryName} - {capitalName}");

print(countries);

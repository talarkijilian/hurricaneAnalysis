# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def update_damages(list_damages):
    conversion = {'M': 1000000, 'B': 1000000000}
    new_damages = []
    for damage in list_damages:
        if damage == 'Damages not recorded':
            new_damages.append(damage)
        elif damage[-1] in conversion:
            new_damages.append(float(damage[:-1]) * conversion[damage[-1]])
    return new_damages

updated_damages = update_damages(damages)
print(update_damages(damages))
print('\n')



# write your construct hurricane dictionary function here:
def create_hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    dictionary = {}
    for i in range(len(names)):
        dictionary[names[i]] = {'Name': names[i], 
                                'Month': months[i], 
                                'Year': years[i], 
                                'Max Sustained Wind': max_sustained_winds[i],
                                'Areas Affected': areas_affected[i],
                                'Damage': updated_damages[i], 
                                'Deaths': deaths[i]}
    return dictionary

hurricanes = create_hurricane_dictionary(names, months, years, max_sustained_winds, 
                                areas_affected, damages, deaths)

print(hurricanes)
print('\n')


# write your construct hurricane by year dictionary function here:
def create_dictionary_year(hurricanes):
    hurricane_year = {}
    for hurricane in hurricanes.values():
        if hurricane['Year'] not in hurricane_year:
            hurricane_year[hurricane['Year']] = [hurricane]
        else:
            hurricane_year[hurricane['Year']].append(hurricane)
    return hurricane_year

hurricane_year = create_dictionary_year(hurricanes)
print(hurricane_year)
print('\n')


# write your count affected areas function here:
def areas_affected_count(hurricanes):
    hurricane_area = {}
    # loop in all the values in the hurricanes dictionary
    for hurricane in hurricanes.values():
        # loop in the area values in the hurricane lists
        for area in hurricane['Areas Affected']:
            if area not in hurricane_area:
                hurricane_area[area] = 1
            else:
                hurricane_area[area] += 1
    return hurricane_area

areas_affected = areas_affected_count(hurricanes)        
print(areas_affected)
print('\n')


# write your find most affected area function here:
def most_affected_area(hurricanes):
    max_count = 0
    max_area = ''
    for area in hurricanes:
        if max_count < hurricanes[area]: 
            max_count = hurricanes[area]
            max_area = area
    return max_area, max_count

max_area, max_area_count = most_affected_area(areas_affected)
print(max_area,max_area_count)
print('\n')


# write your greatest number of deaths function here:
def highest_mortality(dictionary):
    max_mortality = 0
    highest_mortality_hurricane = ''
    for hurricane in dictionary:
        if max_mortality < dictionary[hurricane]['Deaths']:
            max_mortality = dictionary[hurricane]['Deaths']
            highest_mortality_hurricane = hurricane
    return highest_mortality_hurricane, max_mortality

highest_mortality_hurricane, max_mortality = highest_mortality(hurricanes)
print(highest_mortality_hurricane, max_mortality)
print('\n')


# write your catgeorize by mortality function here:
def categorise_by_mortality(hurricanes):
    mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}
    hurricane_mortality = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for hurricane in hurricanes:
        mortality_num = hurricanes[hurricane]['Deaths']
        if mortality_num == mortality_scale[0]:
            hurricane_mortality[0].append(hurricanes[hurricane])
        elif mortality_num > mortality_scale[0] and mortality_num <= mortality_scale[1]:
            hurricane_mortality[1].append(hurricanes[hurricane])
        elif mortality_num > mortality_scale[1] and mortality_num <= mortality_scale[2]:
            hurricane_mortality[2].append(hurricanes[hurricane])
        elif mortality_num > mortality_scale[2] and mortality_num <= mortality_scale[3]:
            hurricane_mortality[3].append(hurricanes[hurricane])
        elif mortality_num > mortality_scale[3] and mortality_num <= mortality_scale[4]:
            hurricane_mortality[4].append(hurricanes[hurricane])
        else:
            hurricane_mortality[5].append(hurricanes[hurricane])
    return hurricane_mortality

hurricane_mortality_scale = categorise_by_mortality(hurricanes)
print(hurricane_mortality_scale)
print('\n')

# write your greatest damage function here:
def greatest_damage(hurricanes):
    max_damages = 0
    max_damage_hurricane = ''
    for data in hurricanes.values():
        try:
            if data['Damage'] > max_damages:
                max_damages = data['Damage']
                max_damage_hurricane = data['Name']
        except:
            continue
    return max_damage_hurricane, max_damages
    
max_damage_hurricane, max_damages = greatest_damage(hurricanes)
print(max_damage_hurricane, max_damages)
print('\n')


# write your catgeorize by damage function here:
def categorise_by_damage(hurricanes):
    damage_scale = {0: 0, 1: 100000000, 2: 1000000000, 3: 10000000000, 4: 50000000000}
    hurricane_damage = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for hurricane in hurricanes:
        damage_count = hurricanes[hurricane]['Damage']
        if damage_count == damage_scale[0] or damage_count == 'Damages not recorded':
            hurricane_damage[0].append(hurricanes[hurricane])
        elif damage_count > damage_scale[0] and damage_count <= damage_scale[1]:
            hurricane_damage[1].append(hurricanes[hurricane])
        elif damage_count > damage_scale[1] and damage_count <= damage_scale[2]:
            hurricane_damage[2].append(hurricanes[hurricane])
        elif damage_count > damage_scale[2] and damage_count <= damage_scale[3]:
            hurricane_damage[3].append(hurricanes[hurricane])
        elif damage_count > damage_scale[3] and damage_count <= damage_scale[4]:
            hurricane_damage[4].append(hurricanes[hurricane])
        else:
            hurricane_damage[5].append(hurricanes[hurricane])
    return hurricane_damage

hurricane_damage_scale = categorise_by_damage(hurricanes)
print(hurricane_damage_scale)
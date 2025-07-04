#Write a python program to demonstrate on how to create a dictonary of dictionaries.
#USe this reference : country = { state: {capital,population} }
#also create sub dictionary

#Dictionary of dictionaries
india = {"Karnataka": {"capital": "Bangalore", "population": 61095297},
         "Maharashtra": {"capital": "Mumbai", "population": 123144223},
         "Tamil Nadu": {"capital": "Chennai", "population": 72147030}
}

print("India's States and Capitals:")
for state, details in india.items():    
    print(f"State: {state}, Capital: {details['capital']}, Population: {details['population']}")

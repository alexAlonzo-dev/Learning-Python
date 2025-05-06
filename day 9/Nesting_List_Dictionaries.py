capitals = {
    "France" : "Paris",
    "Germany" : "Berlin",
}

#Nested List in Dictionary
travel_log = {
    "Mexico" : ["Mexico City", "Zacatecas", "Sinaloa"],
    "URSS" : ["Rusia", "Ucrania", "Bielorrusia"],
}

print(travel_log["URSS"])

print(travel_log["URSS"][0])


#Nested List
nested_list = ["a", "b", ["c", "d"]]
print(nested_list)
print(nested_list[2][1])

#Nesting Dictionary in a Dictionary
travel_log_times = {
    "Mexico" : {
        "times" : 2,
        "citys visited" : ["Mexico City", "Zacatecas", "Sinaloa"],
        },
    "URSS" : {
        "times" : "666",
        "citys visited" : ["Moscu", "San Petesburgo"],
    }  
}

print(f"This would be print Sinaloa, -> {travel_log_times['Mexico']['citys visited'][2]}\nThis would be print Sinaloa, -> {travel_log_times['URSS']['citys visited'][0]}\nThis would be print 666, -> {travel_log_times['URSS']['times']}")
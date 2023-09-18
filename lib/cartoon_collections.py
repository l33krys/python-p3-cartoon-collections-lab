def roll_call_dwarves(list):
    for index, dwarf in enumerate(list):
        print(f"{index+1}. {dwarf}")

def summon_captain_planet(list):
    return [f"{planeteer.title()}!" for planeteer in list]

def long_planeteer_calls(list):
    if len([item for item in list if len(item) > 4]):
        return True
    else:
        return False

def find_the_cheese(list):
    if "cheddar" in list:
        return "cheddar"
    elif "gouda" in list:
        return "gouda"
    elif "camembert" in list:
        return "camembert"
    else:
        return None

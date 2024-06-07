"""mein kraft"""
import math

def mining(damage, health):
    """mining"""
    return math.ceil(damage * (damage / health) * 2)

def special(damage, health):
    """special"""
    return math.floor(mining(damage, health) + 10 * 3)

def tnt(damage, health):
    """tnt"""
    return math.floor((health / 3) * mining(damage, health))

def main():
    """main"""
    health = float(input())
    damage = float(input())
    while health > 0:
        skill = input()
        if not skill:
            break
        if skill == 'Mining':
            damage_dealt = mining(damage, health)
            health -= damage_dealt
            print(f"Use Mining deal {damage_dealt} damage.")
        elif skill == 'Special':
            damage_dealt = special(damage, health)
            health -= damage_dealt
            print(f"Use Special Attack deal {damage_dealt} damage.")
        elif skill == 'TNT':
            damage_dealt = tnt(damage, health)
            health -= damage_dealt
            print(f"Use TNT deal {damage_dealt} damage.")
        else:
            print("We don\'t know that skill.")
        if health > 0:
            print(f"Ore\'s health is {health:.2f}. We need to dig in more.")
        else:
            print(f"Ore\'s health is down to {health:.2f}. We successfully mined the ore.")
            break
main()

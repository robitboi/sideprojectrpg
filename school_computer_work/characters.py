"""character.py
The base class for the player and any NPC's in the game. Will have attributes
and behavior common to all characters
"""

class Character:
    """Any playing and non-Playing chracters share these traits

    Attributes:
        name: a string
        class_name: what type of character class - string 
        strength: int strength attribute as a number
        dexterity: int dexterity attribute
        intelligence: int how smart the character is compare to other characters
        speed: int speed compared to other characters
        charisma: int how able characters are to persuade you or other characters
        wisdom: int characters ability to detect and here things around them
        defense: int charcaters abilty to tank or deflect hits from enemies
        constitution: int health, stamina, etc."""
    
    def __init__(self, name: str, class_name="", strength=0) -> None:
        self.name = name
        self.class_name = class_name
        self.strength = 0
        self.dexterity = 0
        self.intelligence = 0
        self.speed = 0
        self.charisma = 0
        self.wisdom = 0
        self.defense = 0
        self.constitution = 0
    
    def get_stats(self) -> str:
        "return a formatted string of stats"
        stats = f"Name: {self.name}\nClass: {self.class_name}\n"
        stats += f"Strength: {self.strength}\nDexterity: {self.dexterity}"
        stats += f"\nIntelligence: {self.intelligence}\nSpeed: {self.speed}"
        stats += f"\nCharisma: {self.charisma}\nWisdom: {self.wisdom}"
        stats += f"\nDefense: {self.defense}\nConstitution: {self.constitution}"
        return stats 

if __name__ == "__main__":
    player = Character("Steve", "Wizard")
    print(player.get_stats())
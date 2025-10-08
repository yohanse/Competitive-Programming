class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        num_spells, num_potions = len(spells), len(potions)

        spells_index = [i for i in range(num_spells)]
        pairs = [0 for _ in range(num_spells)]

        spells_index.sort(key=lambda x: spells[x])
        potions.sort()

        potion_pointer = num_potions - 1
        for spell_pointer in range(num_spells):
            while potion_pointer > -1 and potions[potion_pointer]*spells[spells_index[spell_pointer]] >= success:
                potion_pointer -= 1
            
            pairs[spells_index[spell_pointer]] = num_potions - potion_pointer - 1
        
        return pairs
        
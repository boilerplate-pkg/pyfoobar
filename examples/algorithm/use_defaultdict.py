
#%%
import collections

def add_animal_in_family(species, animal, family) :
    """
    collections.defaultdict
    """
    species[family].add(animal)

species = collections.defaultdict(set)
add_animal_in_family(species, "cat", "felidea")
print(species)

#%%

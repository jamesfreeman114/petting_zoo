from slithering import Anaconda, Cobra, KingSnake, Python, RattleSnake
from swimming import Barracuda, ElectricEel, GoldFish, Piranha, SwordFish
from walking import Cow, Donkey, Horse, Llama, Pig


bessie =Cow("Bessie", "cow", "mid-day", "Grain")
horace = Donkey("Horace", "donkey", "mid-day", "Oats")
sb = Horse("Sea Bisbuit", "horse", "morning", "Oats")
wilbur = Pig("Wilbur", "pig", "mid-day", "Slop")
miss_fuzz = Llama("Miss Fuzz", "domestic llama", "morning", "Llama Chow" )

miss_fuzz.feed()

print(bessie)
print(horace)
print(sb)
print(wilbur)
print(miss_fuzz)


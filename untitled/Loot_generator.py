class Treasure:
    def __init__(self):
        pass
    def get_pool(self,level):
        if(level==1):
            return ['Battlechest','RustyChainmail','PoorManChest','SteelPlatemail','BarrelArmor','RustySword','Shortsword','Broadsword','WoodenShield','RustyHandgun','StupidFireball','MagicArrow','MagicShield','Frostbite']
        if(level==5):
            return ['LightningBolt','ManaBurst','EarthSpike','PolishedSteelHandgun','IronFist','MithrilArmor','MithrilShortsword','RockCarapace','MagicCape']
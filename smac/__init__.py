from smac.settings import Settings

                
class SMAC:
    def __init__(self, settings: dict = {}):
        settings = Settings(settings)
        print(settings)
    
    def optimize(self):
        pass

class Chosma:
    material="Plastic or Metal"
    def __init__(self,frame_color,lens_type,power):
        self.frame_color=frame_color
        self.lens_type=lens_type
        self.power=power

chosma1=Chosma("Black","Anti-glare",-2)
chosma2=Chosma("Silver","Blue-light",-1.5)


print(chosma1.material,chosma1.frame_color,chosma1.lens_type,chosma1.power)
print(chosma2.power)
print(chosma2.material)
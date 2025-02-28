class Glass:
    material ="glass"  #class attribute

    def __init__(self,color):
      self.color=color

glass1=Glass("Blue")  #obj
print(glass1.material)
print(glass1.color)

print(glass1.material,glass1.color)
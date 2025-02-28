class Computer:
    def config(self):
        print(" Corei5, 12gb")

computer=Computer()
abul=Computer()

computer.config()
abul.config()


Computer.config(abul)

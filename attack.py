class Target:
    power = 5
    def attack(self):
        print('Gah!')
        self.power -= 1

    def checkPower(self):
        if self.power <= 0:
            print('D E S T R O Y E D')
        else:
            print('Power at {}'.format(self.power))

robo1 = Target()
num = int(input('Fire how many shots? '))
while num != 0:
    print('\x1b[31m')
    print('Firing!')
    print('\x1b[m')
    robo1.attack()
    num -= 1
    robo1.checkPower()




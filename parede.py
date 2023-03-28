a = float(input("\033[1;31mQual é a altura da sua parede:"))
l = float(input("\033[1;34mQual é a largura da sua parede:"))
p = a * l
t = p / 2
print("\033[1;32mEssa é adimensão da sua parede {} x {} a sua área é de {:.2f}m².".format(a, l, p))
print("\033[1;32mVocê utilizara {:.2f}litros para pintar sua parede".format(t))
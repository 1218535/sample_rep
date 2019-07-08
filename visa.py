#pyvisaしか入っていないので、それをvisaと直すのを忘れない。
import pyvisa as visa
rm = visa.ResourceManager('@py')
print(rm.list_resources())

print(rm)
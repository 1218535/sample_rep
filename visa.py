#pyvisaしか入っていないので、それをvisaと直すのを忘れない。
import pyvisa as visa
rm = visa.ResourceManager()


#まずは機械を物理的に接続する。そして、
#機械のIPアドレス、品番？（キーサイトのホームページかなんかで調べる）
#をかくにんして打ち込む。
print(rm.list_resources())

print(rm)
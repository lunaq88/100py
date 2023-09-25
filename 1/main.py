name = input("name: ")
cf = int(input("Count from:"))
ct = int(input("Count to:"))+1

dele = open("gen.txt", "w")
dele.close()

for n in range(cf, ct):
        f = open("gen.txt", "a")
        f.writelines([f"{name}{n}\n"])
        f.writelines([f"{name.lower()}{n}\n"])
        f.writelines([f"{name.upper()}{n}\n"])
        f.close()

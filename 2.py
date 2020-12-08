def fuckyouelvesyouruinedmylifelastyear(line):
    a, b, letter, pwd = line.replace('-', ' ').replace(':', '').split(' ')
    return int(a), int(b), letter, pwd
def sled(min_occ, max_occ, letter, pwd):
    return min_occ <= pwd.count(letter) <= max_occ
def toboggan(pos1, pos2, letter, pwd):
    return (pwd[pos1-1] == letter) != (pwd[pos2-1] == letter)
if __name__ == '__main__':
    with open("eatshitelves.dat") as f:
        data = f.read().splitlines()
    print(sum(sled(*fuckyouelvesyouruinedmylifelastyear(line)) for line in data))
    print(sum(toboggan(*fuckyouelvesyouruinedmylifelastyear(line)) for line in data))

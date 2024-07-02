import numpy as np
from random import randint

def write_to_file(path, text): 
    with open(path, "w") as file: 
        file.write(text)

def main():
    rand_numb1 = randint(1, 100)
    rand_numb2 = randint(1, 100)

    result = np.asarray([rand_numb1, rand_numb2]).dot(np.asarray([rand_numb2, rand_numb1]))

    write_to_file("result.txt",str(result))

main()
import sys
class Block:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.st = str(x)+" "+str(y)+" "+str(z)+","


def BA(block):
    return block.x * block.y


def Max_Stack_Height(file0):

    file1 = []
    for i in file0:
        file1.append((i.split()))
    numOfBlocks = len(file1)
    blocks = []  # list of all possible block configurations


    for i in range(numOfBlocks):#Create array of all rotations of all blocks (3 rotations per block)
        blocks.append(Block(int(file1[i][0]), int(file1[i][1]), int(file1[i][2])))
        blocks.append(Block(int(file1[i][1]), int(file1[i][2]), int(file1[i][0])))
        blocks.append(Block(int(file1[i][2]), int(file1[i][0]), int(file1[i][1])))

    blocks.sort(key=BA, reverse=True)#sort boxes in descending order in terms of the area of their base dimensions

    n = len(blocks)
    DPTable = [0] * n
    DPTableT = [""] * n
    for i in range(n):#initialize DPTable (table of maximum stacked blocks height with block [i] on-top) with heights
                        #of each block
        DPTable[i] = blocks[i].z
        DPTableT[i] = blocks[i].st


    for i in range(1, n):#skip the first block (largest base) because it can never go on top of another box
        for j in range(0, i):
            if ((blocks[i].x < blocks[j].x and blocks[i].y < blocks[j].y) or
                    (blocks[i].y < blocks[j].x and blocks[i].x < blocks[j].y)):#if block[i] can stack on top of block[j]

                if DPTable[i] < DPTable[j] + blocks[i].z:#if new height is larger than old height in DPTable
                    DPTable[i] = DPTable[j] + blocks[i].z
                    DPTableT[i] = DPTableT[j] + blocks[i].st

    index = DPTable.index(max(DPTable))

    print("The tallest tower has "+str(len(DPTableT[index][:-1].split(",")))+" blocks and a height of "+str(DPTable[index])+".")
    return DPTableT[index][:-1].split(",")



# Max_Stack_Height()

if __name__ == "__main__":
    f = open(sys.argv[1])
    blocks = []
    for x in f:
        blocks.append(x)
    numOfBlocks = blocks.pop(0)
    f.close()
    stack = Max_Stack_Height(blocks)
    f = open(sys.argv[2], "w")
    f.write(str(len(stack)))
    f.write("\n")
    for x in stack:
        f.write(x)
        f.write("\n") 
    f.close()
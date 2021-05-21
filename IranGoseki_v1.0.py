import csv
import copy


def main():
    syuList = csv.reader(open("In.csv", encoding="utf_8"))
    skillDict = dict(csv.reader(open("SkillList.csv")))

    syuList = [row for row in syuList]

    sameList = []

    for rowA in range(len(syuList)):
        if rowA in sameList:
            continue
        Askill1 = syuList[rowA][0]
        Asize1 = int(0 if Askill1 not in skillDict else skillDict[Askill1])
        Alevel1 = int(syuList[rowA][1])
        Askill2 = syuList[rowA][2]
        Asize2 = int(0 if Askill2 not in skillDict else skillDict[Askill2])
        Alevel2 = int(syuList[rowA][3])
        Aslot1 = int(0 if syuList[rowA][4] == "" else syuList[rowA][4])
        Aslot2 = int(0 if syuList[rowA][5] == "" else syuList[rowA][5])
        Aslot3 = int(0 if syuList[rowA][6] == "" else syuList[rowA][6])
        AslotList = [Aslot1, Aslot2, Aslot3]
        same = 0

        for rowB in range(len(syuList)):
            if rowA == rowB:
                continue
            Bskill1 = syuList[rowB][0]
            Blevel1 = int(syuList[rowB][1])
            Bskill2 = syuList[rowB][2]
            Blevel2 = int(syuList[rowB][3])
            Bslot1 = int(0 if syuList[rowB][4] == "" else syuList[rowB][4])
            Bslot2 = int(0 if syuList[rowB][5] == "" else syuList[rowB][5])
            Bslot3 = int(0 if syuList[rowB][6] == "" else syuList[rowB][6])
            BslotList = [Bslot1, Bslot2, Bslot3]

            level1 = level2 = 0
            level1 += Blevel1 if Askill1 == Bskill1 else 0
            level1 += Blevel2 if Askill1 == Bskill2 else 0
            level2 += Blevel1 if Askill2 == Bskill1 else 0
            level2 += Blevel2 if Askill2 == Bskill2 else 0

            if ((Askill1 == Bskill1 and Alevel1 == Blevel1 and Askill2 == Bskill2 and Alevel2 == Blevel2) or
               (Askill1 == Bskill2 and Alevel1 == Blevel2 and Askill2 == Bskill1 and Alevel2 == Blevel1)) and \
               Aslot1 == Bslot1 and Aslot2 == Bslot2 and Aslot3 == Bslot3:
                same = rowB
                continue

            while level1 < Alevel1:
                for i in range(0, 3):
                    if Asize1 <= BslotList[2-i]:
                        level1 += 1
                        BslotList[2-i] = 0
                        break
                else:
                    break

            while level2 < Alevel2:
                for i in range(0, 3):
                    if Asize2 <= BslotList[2-i]:
                        level2 += 1
                        BslotList[2-i] = 0
                        break
                else:
                    break

            if level1 >= Alevel1 and level2 >= Alevel2:
                slotList = copy.copy(AslotList)
                for i in range(0, 3):
                    if slotList[i] <= BslotList[i]:
                        slotList[i] = 0

                if sum(slotList) == 0:
                    syuList[rowA].append(rowB + 1)
                    break
        else:
            if same:
                sameList.append(same)
                syuList[rowA].append(-(same + 1))

    f = open('Out.csv', 'w', encoding="utf_8", newline='')
    writer = csv.writer(f)
    for row in syuList:
        writer.writerow(row)
    f.close()


main()

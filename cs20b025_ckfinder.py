import itertools


def getClosure(reqSet, fdMap):
    """
    Returns the Closure of reqSet given functional dependencies in the form of list of sets
    """
    reqSet = set(reqSet)  # for type support
    fdMap = list(fdMap)  # for type support

    for _ in range(2):
        # The order in which fd's map through reqSet is random , so running two times ensures all the possible combination is covered
        for fd in fdMap:
            fdLeft = set(fd[0])
            fdRight = set(fd[1])

            # If the fdLeft is a subset of reqSet and the fdRight is not in reqSet then the reqSet is updated
            # that means fdRight has some attribute which is not present in reqSet
            if fdLeft.issubset(reqSet) and len(fdRight.difference(reqSet)) != 0:
                reqSet.update(fdRight)

    return reqSet


def DrawLine(count, req):
    for _ in range(count):
        print(req, end="")


if __name__ == "__main__":
    fdFileNameList = ["cs20b025_fd.txt", "cs20b025_input1NF.txt",
                      "cs20b025_input2NF.txt", "cs20b025_input3NF.txt", "cs20b025_inputBCNF.txt"]
    for fdFileName in fdFileNameList:
        fileHandle = open(fdFileName, 'r')
        fileContent = fileHandle.readlines()

        allVars = fileContent[0]
        fdCount = int(fileContent[1])
        fdmap = []
        rules = {"1NF": "we can assume every fd obey it becoz it is our preference",
                 "2NF": "cycle in functional dependencies required because we shouldn't have partial dependencies",
                 "3NF": "it must contain cycle as well (it obeys 2NF) but cycle of length more than 2 gets transitive dependency so we need to avoid it, thus cycle length must always be 2",
                 "BCNF": "any valid 2NF can be considered BCNF", "other": "no rule"}

        fds = fileContent[2:]
        # Add all the FDs in the list of FDs to the FDMap.
        for fd in fds:
            index = fd.index(",")
            fdLeft = fd[0:index].strip()
            fdRight = fd[index+1:].strip()
            fdmap.append((set(fdLeft), set(fdRight)))

        """
        generate all possible combinations of attributes
        find if any of the combination is super key and check 
        if it is minimal , then add it as candidate key
        """
        allVars = allVars.strip()
        allVars = frozenset(allVars)
        candidateKeys = []

        # Returns a list of combinations of combinations of the same length as allVars.
        for combLen in range(1, len(allVars)+1):

            # Collect all combinations of combinations.
            for comb in itertools.combinations(allVars, combLen):
                preClosure = getClosure(comb, fdMap=fdmap)

                # Check whether the closure we get actually a super key.
                if preClosure == allVars:
                    super_key = comb
                    is_minimal = True
                    # Check whether super_key is actually minimal
                    for preCk in candidateKeys:
                        preCk = set(preCk)
                        # If the comb is a minimal combination.
                        if preCk.issubset(super_key):
                            is_minimal = False

                    # Add a candidate key to candidateKeys list.
                    if is_minimal:
                        candidateKeys.append(super_key)

        reqCount = 40
        DrawLine(reqCount, "=")
        print("\nInput [{0}]".format(fdFileName))
        print("Functional dependencies")

        for value in fdmap:
            xl, xr = value
            print("{0} ==> {1}".format(xl,xr))

        print("\nCandidate Keys")

        for index, value in enumerate(candidateKeys):
            print("{0:>2}) {1}".format(index+1, "".join(list(value))))

        if fdFileName.find("1NF") != -1:
            print("\nRule: {0}".format(rules["1NF"]))
        elif fdFileName.find("2NF") != -1:
            print("\nRule: {0}".format(rules["2NF"]))
        elif fdFileName.find("3NF") != -1:
            print("\nRule: {0}".format(rules["3NF"]))
        elif fdFileName.find("BCNF") != -1:
            print("\nRule: {0}".format(rules["BCNF"]))
        else:
            print("\nRule: {0}".format(rules["other"]))

        print("\nPrime Attributes")
        primeAttr = set()
        for value in candidateKeys:
            primeAttr.update(value)
        print("".join(sorted(list(primeAttr))))

        print("\nNon-Prime Attributes")

        nonPrim = allVars.difference(primeAttr)
        if len(nonPrim) == 0:
            print("None")
        else:
            print("".join(nonPrim))

        DrawLine(reqCount, "=")

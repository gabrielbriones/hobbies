list_pkgs_avx2 = []
list_pkgs_avx512 = []

pkg = ""

import os

#os.system("grep -R '/haswell/' &> log")

with open('log') as f:
    lines = f.readlines()
    for line in lines:
        if ".spec" in line:
            if "/haswell"in line and "/avx512" not in line and "#" not in line:
                pgk = line.split("/")[0]
                list_pkgs_avx2.append(pgk)

            if "/avx512" in line and "#" not in line:
                pgk = line.split("/")[0]
                list_pkgs_avx512.append(pgk)
    print()
    print("packages with avx2")
    for element in sorted(set(list_pkgs_avx2)):
        print (element)

    print()
    print("packages with avx512")
    for element in sorted(set(list_pkgs_avx512)):
        print (element)

    print()
    print("packages w avx2 but no avx512")
    for element in sorted(list(set(list_pkgs_avx2) - set(list_pkgs_avx512))):
        print(element)
        


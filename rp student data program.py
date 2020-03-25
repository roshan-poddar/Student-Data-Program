print("WELCOME TO RP DATA")
a = input("You want to run our program:")
b = input("Tell your name for better communication:")
def rp():
    print(b+""" We gives you four option
           1.You want to create a new file and add data
           2.You want to add data in existing file
           3.You want to display the data
           4.Exit""")
    c = input(b+" Which option you want:")
    if c == "1":
        d = input(b+" enter the name of the file without extension:")
        e = d+'.txt'
        fobj = open(e,'a+')
        if not fobj:
            print(b+" your file is not created")
            f = input(b+" you want to reuse our program:")
            if "y" in f or "yes" in f or "Y" in f or "Yes" in f:
                print(rp())
            if "n" in f or "no" in f or "N" in f or "No" in f:
                print(exit())
        else:
            fobj = open(e,'a+')
            g = input("Enter the student name:")
            h = input("Enter the roll no.:")
            i = input("Enter the class:")
            fobj.write(g)
            fobj.write(h)
            fobj.write(i+'\n')
            fobj.close()
            f = input(b+" you want to reuse our program:")
            if "y" in f or "yes" in f or "Y" in f or "Yes" in f:
                print(rp())
            if "n" in f or "no" in f or "N" in f or "No" in f:
                print(exit())
        fobj.close()
    elif c == "2":
        j = input(b+" enter the name of the existing file:")
        k = j+'.txt'
        fobj = open(k,'a+')
        if not fobj:
            print(b+" Your file is not created")
            f = input(b+" you want to reuse our program:")
            if "y" in f or "yes" in f or "Y" in f or "Yes" in f:
                print(rp())
            if "n" in f or "no" in f or "N" in f or "No" in f:
                print(exit())
        else:
            fobj = open(k,'a+')
            l = input("Enter the name:")
            m = input("Enter the roll no.:")
            n = input("Enter the class:")
            fobj.write(l)
            fobj.write(m)
            fobj.write(n+'\n')
            fobj.close()
            f = input(b+" you want to reuse our program:")
            if "y" in f or "yes" in f or "Y" in f or "Yes" in f:
                print(rp())
            if "n" in f or "no" in f or "N" in f or "No" in f:
                print(exit())
        fobj.close() 
    elif c == "3":
        o = input(b+" enter the file name which you want to display:")
        p = o+'.txt'
        fobj = open(p,'r')
        data = fobj.read()
        print(data)
        f = input(b+" you want to reuse our program:")
        if "y" in f or "yes" in f or "Y" in f or "Yes" in f:
            print(rp())
        if "n" in f or "no" in f or "N" in f or "No" in f:
            print(exit())
        fobj.close()
    elif c == "4":
        print(exit())
    else:
        print(b+" you entered something wrong")
        f = input(b+" you want to reuse our program:")
        if "y" in f or "yes" in f or "Y" in f or "Yes" in f:
            print(rp())
        if "n" in f or "no" in f or "N" in f or "No" in f:
            print(exit())
rp()
import os

def j_caller(k_number, algo):
    """
    Calls the java jar to perform the CHkS algorithm on the data
    :return:
    """

    #Number of vertices
    k_number = str(k_number)
    print("Number of vertices is:", k_number)
    print("Algorithm chosen:", algo)

    #Define command
    cmd = "java -jar ../jar/CHkS.jar %s"%algo +" ../pythonProject/bow.txt %s" % k_number

    #Call command
    os.system(cmd)
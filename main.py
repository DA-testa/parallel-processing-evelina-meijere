# python3

def parallel_processing(n, m, data):
    output = []
    laiks = list(data)
    thread = [0] * n 

    for i in range(m):
        nakamais = min(range(n), key = lambda x: thread[x])
        out.append((nakamais, i))
        thread[nakamais] += laiks[i]

    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs

    return output

def main():
    n, m = map(int,input().split())
    data = list(map(int, input(). split()))
    result = parallel_processing(n,m,data)
    for pari in result:
        print(pari[0],pari[1])
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n = 0
    m = 0

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = []

    # TODO: create the function
    
    
    # TODO: print out the results, each pair in it's own line



if __name__ == "__main__":
    main()

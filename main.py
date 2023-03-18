# python3

def parallel_processing(n, m, data):
    output = []
    laiks = list(data)
    thread = [0] * n 

    for i in range(m):
        nakamais = thread.index(min(thread))
        output.append((nakamais, i))
        thread[nakamais] += laiks[i]
        
   
    return output

def main():
    try:
        n, m = map(int,input().split())
        data = list(map(int, input().split()))
        output = parallel_processing(n,m,data)
        for pari in output:
            print(pari[0],pari[1])
    except ValueError:
        print("Kļūda ievadē")
  
if __name__ == "__main__":
    main()

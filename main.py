# python3
import heapq

def parallel_processing(n, m, data):
    output = []
    p = [(0, j) for j in range(n)]
    heapq.heapify(p)

    for p op in enumarate(data):
       laiks, b = heapq.heappop(p)
       output.append((b,laiks))
       heapq.heappush(p,(laiks + op, thread))
          
    return output

def main():
        n, m = map(int,input().split())
        data = list(map(int, input().split()))
        result = parallel_processing(n,m,data)
        for p time in result:
            print(p, time)
    
if __name__ == "__main__":
    main()

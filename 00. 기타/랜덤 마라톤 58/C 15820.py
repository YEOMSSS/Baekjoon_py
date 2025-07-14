import sys
input = sys.stdin.readline

def main():
    S1, S2 = map(int, input().split())

    sample_miny = [tuple(map(int, input().split())) for _ in range(S1)]
    system_miny = [tuple(map(int, input().split())) for _ in range(S2)]

    
    for sample, miny in sample_miny:
        if sample != miny:
            print("Wrong Answer")
            return

    for system, miny in system_miny:
        if system != miny:
            print("Why Wrong!!!")
            return
        
    print("Accepted")

if __name__ == "__main__":
    main()
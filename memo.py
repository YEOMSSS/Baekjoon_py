def main():
    import io
    import os

    # 초고속 입력 (BufferedReader + 큰 버퍼)
    input = io.BufferedReader(io.FileIO(0), 1 << 18).readline

    N, M, K = map(int, input().split())
    R = M + 2  # row 길이 + padding 2 (좌우 경계)

    # 맵 초기화: 상하좌우 padding을 1('1')로 채움
    mp = bytearray([49]) * ((N + 2) * R)  # '1' = 49

    for i in range(1, N + 1):
        mp[i * R + 1 : (i + 1) * R - 1] = input().strip()
        mp[i * R + R - 1] = 49  # 오른쪽 끝 패딩도 '1'

    # 방문배열: 초기값 255(최댓값), 각 위치에 도달할 때 최소 벽 부순 수 기록
    v = bytearray([255]) * len(mp)
    v[:R] = bytearray(R)       # 위쪽 패딩 무시
    v[-R:] = bytearray(R)      # 아래쪽 패딩 무시
    for i in range(1, N + 1):  # 좌우 패딩도 무시
        v[i * R] = 0
        v[i * R + R - 1] = 0

    q = [R + 1]  # 시작점 (1,1) == R+1
    v[R + 1] = 0
    d = 1        # 시작 칸 포함 거리
    end = N * R + M  # (N, M) 위치

    # BFS
    while q and v[end] > K:
        nxt = []
        for j in q:
            k = v[j]

            # 상하좌우 4방향 이동
            for t in (j + R, j - R, j + 1, j - 1):
                vn = k + (mp[t] & 1)
                if v[t] > vn <= K:
                    v[t] = vn
                    nxt.append(t)
        q = nxt
        d += 1

    # 출력 최적화
    os.write(1, str(-1 if v[end] > K else d).encode('ascii'))
    os._exit(0)

main()

#include <stdio.h>
#include <stdlib.h>

// qsort 비교 함수
int compare(const void *a, const void *b) {
    int num1 = *(int*)a;
    int num2 = *(int*)b;
    if (num1 < num2) return -1; // a가 b보다 작다(앞이다)
    else if (num1 > num2) return 1; // a가 b보다 크다(뒤다)
    else return 0; // 같으면 변동이 필요 없다
}

int main() {
    int N, M;
    scanf("%d %d", &N, &M);

    int size = N + M;
    int *arr = malloc(size * sizeof(int));

    // 배열 A 입력
    for (int i = 0; i < N; i++) {
        scanf("%d", &arr[i]);
    }

    // 배열 B 입력
    for (int i = 0; i < M; i++) {
        scanf("%d", &arr[N + i]);
    }

    // qsort로 정렬
    qsort(arr, size, sizeof(int), compare);

    // 출력
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }

    free(arr);
    return 0;
}

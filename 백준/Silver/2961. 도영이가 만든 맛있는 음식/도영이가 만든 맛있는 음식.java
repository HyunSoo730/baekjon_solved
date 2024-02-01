import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static int n;
    static int[] dataA, dataB;
    static int res = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        dataA = new int[n];
        dataB = new int[n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            dataA[i] = Integer.parseInt(st.nextToken());
            dataB[i] = Integer.parseInt(st.nextToken());
        }
        DFS(0,1, 0, 0);  // sumA는 1부터 시작해야함.
        System.out.println(res);
    }

    // * sumA는 신맛, sumB는 쓴맛, cnt는 사용한 개수
    public static void DFS(int L, int sumA, int sumB, int cnt) {
        if (L == n) { // 모두 확인 -> 종료조건
            // 다 탐색했을 때 하나의 재료라도 사용했는지 예외처리
            if(cnt < 1) return;
            if (Math.abs(sumA - sumB) < res) {
                res = Math.abs(sumA - sumB);
            }
        } else {
            DFS(L + 1, sumA * dataA[L], sumB + dataB[L], cnt + 1);  // 현재 재료 사용 (부분집합 포함)
            DFS(L + 1, sumA, sumB, cnt); // 현재 재료 사용X(부분집합 포함 X)
        }
    }
}
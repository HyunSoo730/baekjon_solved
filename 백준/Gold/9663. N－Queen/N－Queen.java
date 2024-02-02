import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static int n;
    static int[] data;
    static int cnt;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        data = new int[n];  // idx에 열, 값에 행을 넣어줌
        DFS(0);
        System.out.println(cnt);
    }

    public static void DFS(int L) {
        if (L == n) { // 마지막까지 도달 -> 종료조건
            cnt += 1;
        } else {
            for (int i = 0; i < n; i++) {  // 가능한 위치 찾기
                data[L] = i;  // 일단 현재 열에 값(행) 넣어두고. 즉 (행(i), 열(L)) 좌표가 가능하다고 해놓고 판단 진행
                if (isValid(L)) {
                    DFS(L + 1);
                }
            }
        }
    }

    public static boolean isValid(int L) {  // 현재 열의 값을 받아옴
        for (int i = 0; i < L; i++) { // 이전 열들까지 (값)행이 같은지
            if (data[L] == data[i]) { // 행이 같은 행이면 놓을 수 없음
                return false;
            } else if (Math.abs(L - i) == Math.abs(data[L] - data[i])) {  // 대각선 판단. 열의 차 와 행의 차가 같으면 같은 대각선
                return false;
            }
        }
        return true;
    }
}
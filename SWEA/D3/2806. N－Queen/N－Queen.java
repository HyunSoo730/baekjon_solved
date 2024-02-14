import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

    static int T, n;
    static int[] data;
    static int cnt;
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        T = Integer.parseInt(br.readLine());

        for (int t = 1; t <= T; t++) {
            n = Integer.parseInt(br.readLine());
            data = new int[n];
            visited = new boolean[n];
            cnt = 0;
            DFS(0);
            System.out.println("#" + t + " " + cnt);
        }
    }

    public static void DFS(int L) {
        if (L == n) {  // 모든 열에 놨음
            cnt += 1;
        } else {
            for (int row = 0; row < n; row++) {
                if(visited[row]) continue;  // 해당 행을 이미 놓았다면 끝
                data[L] = row;   // (row, L) 행, 열 저장
                if (isValid(L)) { // 해당 열에 놓으면 괜찮은지 판단
                    visited[row] = true;
                    DFS(L+1);
                    visited[row] = false;  // 백트랙킹 시 원상복구
                }
            }
        }
    }

    public static boolean isValid(int col) {  // 해당 열에 놓아도 되는지 확인
        for (int i = 0; i < col; i++) {
            if (data[col] == data[i]) {  // 같은 행인지
                return false;
            }
            if (Math.abs(data[col] - data[i]) == Math.abs(col - i)) { // 같은 대각선인지
                return false;
            }
        }
        return true;
    }
}
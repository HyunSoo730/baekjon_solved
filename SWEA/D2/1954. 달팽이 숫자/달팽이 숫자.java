import java.io.*;
import java.util.StringTokenizer;

public class Solution {

    static int n;
    static int[][] board;
    static StringBuilder sb;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            n = Integer.parseInt(br.readLine());
            snail(n);
            check(i+1, n);
        }
    }

    public static void snail(int n) {
        int left = -1;
        int right = n-1;
        int top = 0;
        int bottom = n-1;

        board = new int[n][n];
        int k = 1;

        while(k <= n*n){
            // 1. 왼쪽 -> 오른쪽 방향 실행
            left += 1;
            for (int i = left; i <= right;i++) {
                board[top][i] = k++;
            }
            // 2. 오른쪽 -> 오른쪽 아래 방향 실행
            top += 1;
            for (int i = top; i <= bottom; i++) {
                board[i][right] = k++;
            }
            // 3. 오른쪽 아래 -> 왼쪽 아래 방향 실행
            right -=1;
            for (int i = right; i >= left; i--) {
                board[bottom][i] = k++;
            }
            // 4. 왼쪽 아래 -> 왼쪽 위 방향 실행
            bottom -=1;
            for (int i = bottom; i >= top; i--) {
                board[i][left] = k++;
            }
        }
    }

    public static void check(int t, int n) {
        sb = new StringBuilder();
        sb.append("#").append(t).append("\n");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                sb.append(board[i][j]).append(" ");
            }
            if (i != n - 1) {
                sb.append("\n");
            }
        }
        System.out.println(sb);
    }

}
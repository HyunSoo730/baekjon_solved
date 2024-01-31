import java.io.*;
import java.util.StringTokenizer;

/**
 * @author 조현수
 * @date 24.1.31
 * @link 백준_11660_구간합구하기5
 * @keyword_solution  2차원 구간합 (누적합) -> 행별로 구간합을 저장해야함.
 * @input 
 * @output
 * @time_complex
 * @perf 메모리 ~, 소요시간 ~
 */
public class Main {
    static int n, m;  // 크기 n, 구간합 횟수 m
    static int[][] data;
    static int[][] dp;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        data = new int[n+1][n+1];
        dp = new int[n+1][n+1];
        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= n; j++) {
                data[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i = 1; i <= n; i++) {
            dp[i][1] = data[i][1];
        }
        for (int i = 1; i <= n; i++) {
            for (int j = 2; j <= n; j++) {
                dp[i][j] = dp[i][j-1] + data[i][j];
            }
        }

        // 각 행별로 구간합 구해놓고 계산 진행

        int startX, startY, endX, endY;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < m; i++) {
            int sum = 0;
            st = new StringTokenizer(br.readLine());
            startX = Integer.parseInt(st.nextToken());
            startY = Integer.parseInt(st.nextToken());
            endX = Integer.parseInt(st.nextToken());
            endY = Integer.parseInt(st.nextToken());

            for (int x = startX; x <= endX; x++) {
                sum += dp[x][endY] - dp[x][startY-1];
            }
            sb.append(sum).append("\n");
        }
        System.out.println(sb);

    }
}
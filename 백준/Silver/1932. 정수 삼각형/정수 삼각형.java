import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    static int n;
    static int[][] data, dp;

    // ! 아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택 가능
    // ! 굳이 규격에 맞게 배열을 만들 필요가 없었음 -> [n+1][n+1]로 만들어도 충분하다.
    public static void main(String[] args) throws IOException {

        n = Integer.parseInt(br.readLine());
        // 현재의 선택이 나중의 선택에 영향을 끼침 -> dp
        data = new int[n+1][n+1];
        dp = new int[n+1][n+1];

        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= i; j++) {
                data[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        dp[1][1] = data[1][1];  // 자명한 값
        for (int i = 2; i <= n; i++) {
            for (int j = 1; j <= i; j++) {
                if (j == 1) dp[i][j] = dp[i - 1][j] + data[i][j];
                else if (j == i) dp[i][j] = dp[i - 1][j - 1] + data[i][j];
                else dp[i][j] = Math.max(dp[i - 1][j - 1], dp[i - 1][j]) + data[i][j];
            }
        }

        int res = 0;
        for (int i = 1; i <= n; i++) {
            res = Math.max(res, dp[n][i]);
        }
        System.out.println(res);
//        System.out.println(Arrays.toString(dp[n]));
    }
}
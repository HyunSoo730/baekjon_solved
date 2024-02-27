import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    static int n, INF = Integer.MAX_VALUE;
    static int[] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        dp = new int[n + 1];
        Arrays.fill(dp, INF);
        dp[0] = 0;  // ! 0을 만드는데 횟수 0
        dp[1] = 0;  // 1은 1을 만드는데 0번 필요
        // ! dp[i]는 i를 1로 만드는데 걸리는 최소 횟수

        for (int i = 2; i <= n; i++) {
//            System.out.println("변화 전 : dp[" + i + "] : " + dp[i]);
            dp[i] = Math.min(dp[i - 1] + 1, dp[i]);  // ! 1을 뺏을 때
            if (i % 3 == 0) {
                dp[i] = Math.min(dp[i / 3] + 1, dp[i]);  // 기본값 vs i%3 + 1
            }
            if (i % 2 == 0) {
                dp[i] = Math.min(dp[i / 2] + 1, dp[i]);
            }
//            System.out.println("dp[" + i + "] : " + dp[i]);
        }

        System.out.println(dp[n]);
    }
}
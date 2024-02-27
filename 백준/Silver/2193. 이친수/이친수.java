import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    static int n;
    static long[][] dp;
    static int zero = 0, one = 1;
    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        dp = new long[n+1][2];
        dp[1][zero] = 0;
        dp[1][one] = 1;  // !자명한 값 초기화

        for (int i = 2; i <= n; i++) {
            dp[i][zero] = dp[i - 1][zero] + dp[i - 1][one];
            dp[i][one] = dp[i - 1][zero];  // ! 0로부터만 올 수 있음
        }

        long sum = dp[n][zero] + dp[n][one];
        System.out.println(sum);
    }


}
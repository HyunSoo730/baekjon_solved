import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {


    // ! 집이 n개, R,G,B 중 하나로 칠해야 한다. 해당 집을 칠하는 비용이 주어짐

    /**
     * ! 조건 1. 1번 집의 색 != 2번 집의 색
     * ! 조건 2. N번 집의 색 != N-1번 집의 색
     * ! 2<=i<=n-1, i번 집의 색 != i-1, i+1집의 색
     * * 결국 본인 색과는 다른 집을 골라야 한다는 뜻.
     */
    static int n, INF = 10000000;
    static int red = 0, green = 1, blue = 2;  // 미리 정해두고
    static int[][] dp, data;  // n개의 집에 각각 RGB값 가지도록.
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        dp = new int[n + 1][3];
        data = new int[n + 1][3];
        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken());
            int g = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            // 인덱스를 색깔로 구분하면 돼 0 을 빨강 1을 초록 2를 파랑으로 해서 진행
            data[i][red] = r;
            data[i][green] = g;
            data[i][blue] = b;
        }
        // * n=1인 경우는 dp에 그대로 저장해도 된다. 자명
        dp[1][red] = data[1][red];
        dp[1][green] = data[1][green];
        dp[1][blue] = data[1][blue];
        for (int i = 2; i <= n; i++) {
            dp[i][red] = data[i][red] + Math.min(dp[i - 1][green], dp[i - 1][blue]);
            dp[i][green] = data[i][green] + Math.min(dp[i - 1][red], dp[i - 1][blue]);
            dp[i][blue] = data[i][blue] + Math.min(dp[i - 1][red], dp[i - 1][green]);
        }
        int res = Integer.MAX_VALUE;
        for (int i = 0; i < 3; i++) {
            res = Math.min(res, dp[n][i]);
        }
        System.out.println(res);
    }
}
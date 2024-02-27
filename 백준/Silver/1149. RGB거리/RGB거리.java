import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static int n;
    static int red = 0, green = 1, blue = 2;
    static int[][] dp, data;  // ! 2차원인 이유 : 각 집마다 3개의 값 가질 수 있음 : R,G,B
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        dp = new int[n+1][3]; // ! 1번 인덱스부터 사용
        data = new int[n+1][3];
        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken());
            int g = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            data[i][red] = r;
            data[i][green] = g;
            data[i][blue] = b;
        }

        dp[1][red] = data[1][red];
        dp[1][green] = data[1][green];
        dp[1][blue] = data[1][blue];
        // ! 자명한 값 초기화

        // ! dp[i][j] : i번째 집의 j번째 색(r,g,b)을 칠할 때의 최소값
        for (int i = 2; i <= n; i++) {
            dp[i][red] = Math.min(dp[i - 1][green], dp[i - 1][blue]) + data[i][red];
            dp[i][green] = Math.min(dp[i - 1][red], dp[i - 1][blue]) + data[i][green];
            dp[i][blue] = Math.min(dp[i - 1][red], dp[i - 1][green]) + data[i][blue];
        }

        int min = Integer.MAX_VALUE;
        for (int i = 0; i < 3; i++) {
            min = Math.min(dp[n][i], min);
        }
        System.out.println(min);
    }
}
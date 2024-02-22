import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int n;
    // ! 바로 아래의 수로 넘어가거나, 아니면 바로 아래의 수와 붙어 있는 수로만 이동 가능
    static int[][] data, dp1,dp2;
    public static void main(String[] args) throws IOException {
//        System.setIn(new FileInputStream("input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        data = new int[100001][3];
        dp1 = new int[100001][3];
        dp2 = new int[100001][3];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 3; j++) {
                data[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        dp1[0][0] = data[0][0];
        dp1[0][1] = data[0][1];
        dp1[0][2] = data[0][2];
        dp2[0][0] = data[0][0];
        dp2[0][1] = data[0][1];
        dp2[0][2] = data[0][2];
        // 자명한 사실
        for (int i = 1; i < n; i++) {
            dp1[i][0] = Math.max(dp1[i-1][0], dp1[i-1][1]) + data[i][0];
            dp1[i][1] = Math.max(Math.max(dp1[i-1][0], dp1[i-1][1]), dp1[i-1][2]) + data[i][1];
            dp1[i][2] = Math.max(dp1[i-1][1], dp1[i-1][2]) + data[i][2];

            dp2[i][0] = Math.min(dp2[i-1][0], dp2[i-1][1]) + data[i][0];
            dp2[i][1] = Math.min(Math.min(dp2[i-1][0], dp2[i-1][1]), dp2[i-1][2]) + data[i][1];
            dp2[i][2] = Math.min(dp2[i-1][1], dp2[i-1][2]) + data[i][2];
        }

        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        for (int i = 0; i < 3; i++) {
            max = Math.max(max, dp1[n - 1][i]);
            min = Math.min(min, dp2[n - 1][i]);
        }

        System.out.println(max + " " + min);
    }

}
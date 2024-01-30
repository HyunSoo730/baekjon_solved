import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int n;
    static int[][] data;
    static int T;
    public static void main(String[] args) throws IOException {
        T = Integer.parseInt(br.readLine());
        for (int t = 1; t <= T; t++) {
            n = Integer.parseInt(br.readLine());
            data = new int[n][n];
            for (int i = 0; i < n; i++) {
                String temp = br.readLine();
                for (int j = 0; j < n; j++) {
                    data[i][j] = temp.charAt(j) - '0';
                }
            }
            int res = cal();
            System.out.println("#" + t + " " + res);
        }

    }

    public static int cal() {
        int res = 0;
        int s,e;
        s = e = n /2;
        for (int i = 0; i < n; i++) {
            for (int j = s; j < e+1; j++) {
                res += data[i][j];
            }
            if (i < n / 2) {
                s -= 1;
                e += 1;
            } else {
                s += 1;
                e -= 1;
            }
        }
        return res;
    }
}
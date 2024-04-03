import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    static int T, k;
    static int[][] data;

    public static void rotate(int v, int d) {
        int[] dirs = new int[5];
        dirs[v] = d;

        // 왼쪽 자석 회전 여부 확인
        for (int i = v; i > 1; i--) {
            if (data[i][6] != data[i-1][2]) {
                dirs[i-1] = -dirs[i];
            } else {
                break;
            }
        }

        // 오른쪽 자석 회전 여부 확인
        for (int i = v; i < 4; i++) {
            if (data[i][2] != data[i+1][6]) {
                dirs[i+1] = -dirs[i];
            } else {
                break;
            }
        }

        // 자석 회전
        for (int i = 1; i <= 4; i++) {
            if (dirs[i] == 1) {
                int temp = data[i][7];
                for (int j = 7; j > 0; j--) {
                    data[i][j] = data[i][j-1];
                }
                data[i][0] = temp;
            } else if (dirs[i] == -1) {
                int temp = data[i][0];
                for (int j = 0; j < 7; j++) {
                    data[i][j] = data[i][j+1];
                }
                data[i][7] = temp;
            }
        }
    }

    public static void main(String[] args) throws IOException {
        T = Integer.parseInt(br.readLine());
        for (int t = 1; t <= T; t++) {
            k = Integer.parseInt(br.readLine());
            data = new int[5][8];
            for (int i = 1; i <= 4; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < 8; j++) {
                    data[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            for (int i = 0; i < k; i++) {
                st = new StringTokenizer(br.readLine());
                int v = Integer.parseInt(st.nextToken());
                int d = Integer.parseInt(st.nextToken());
                rotate(v, d);
            }

            int res = 0;
            for (int i = 1; i <= 4; i++) {
                if (data[i][0] == 1) {
                    res += Math.pow(2, i - 1);
                }
            }
            System.out.println("#" + t + " " + res);
        }
    }
}
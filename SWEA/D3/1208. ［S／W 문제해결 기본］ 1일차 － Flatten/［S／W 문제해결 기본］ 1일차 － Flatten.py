import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {

    static int[] data;
    static int n; // 덤프 횟수
    static int MAX_size = 100;

    static int T = 10;
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        for (int t = 1; t <= T; t++) {
            n = Integer.parseInt(br.readLine()); // 덤프 횟수
            st = new StringTokenizer(br.readLine());
            data = new int[100];
            for (int i = 0; i < 100; i++) {
                data[i] = Integer.parseInt(st.nextToken());
            }
            int cnt = cal(data, n);
            System.out.println("#" + t + " " + cnt);

        }
    }

    public static int cal(int[] data, int dump) {
        Arrays.sort(data);
        for (int i = 0; i < dump; i++) {
            if (data[MAX_size - 1] - data[0] <= 1) {
                break;
            }
            data[0] += 1;
            data[MAX_size-1] -=1;
            Arrays.sort(data);
        }
        return data[MAX_size-1] - data[0];
    }
}
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static int n,m; // 수의 개수 n, 합을 구해야 하는 횟수 m
    static int[] data;
    static int[] sum;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        data = new int[n+1];
        sum = new int[n+1];
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= n; i++) {
            data[i] = Integer.parseInt(st.nextToken());
        }
        sum[1] = data[1];
        for (int i = 2; i <= n; i++) {
            sum[i] = data[i] + sum[i-1];
        }
        // 구간 합 저장한 배열 sum
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            System.out.println(sum[e] - sum[s - 1]);
        }
    }
}
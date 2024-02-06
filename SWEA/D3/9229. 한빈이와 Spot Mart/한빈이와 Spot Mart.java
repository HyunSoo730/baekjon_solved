import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

    static int t,n,m;  // 과자 개수, 무게 합 제한
    static int[] data;

    // 과자 2개 선택.
    static int res;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        t = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= t; tc++) {
            st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());  // 과자 개수
            m = Integer.parseInt(st.nextToken());  // 과자 봉지 무게 합
            data = new int[n];
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                data[i] = Integer.parseInt(st.nextToken());
            }
            res = -1;
            DFS(0, 0, 0);

            System.out.println("#" + tc + " " + res);
        }
    }

    public static void DFS(int start, int L, int weight) {
        if (L == 2) {
            if(weight <= m)
                res = Math.max(res, weight);
        } else {
            for (int i = start; i < n; i++) {
                DFS(i + 1, L + 1, weight + data[i]);
            }
        }
    }

}
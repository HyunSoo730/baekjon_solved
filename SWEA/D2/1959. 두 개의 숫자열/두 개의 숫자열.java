import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Solution
{
    static int n,m;
    static int[] dataA, dataB;
    public static void main(String args[]) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int T;
        T = Integer.parseInt(br.readLine());
        for(int test_case = 1; test_case <= T; test_case++)
        {
            st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());
            dataA = new int[n];
            dataB = new int[m];
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                dataA[i] = Integer.parseInt(st.nextToken());
            }
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < m; i++) {
                dataB[i] = Integer.parseInt(st.nextToken());
            }
            int res = maxResult();
            System.out.println("#" + test_case + " " + res);
        }
    }

    public static int maxResult() {
        int res = 0;
        if (n < m) {
            for (int i = 0; i < m - n + 1; i++) {
                int sum = 0;
                for (int j = 0; j < n; j++) {
                    sum += dataA[j] * dataB[i+j];  //B의 더해지는 위치 조정.
                }
                res = Math.max(res, sum);
            }
        } else if (n > m) {
            for (int i = 0; i < n - m + 1; i++) {
                int sum = 0;
                for (int j = 0; j < m; j++) {
                    sum += dataA[i + j] * dataB[j];
                }
                res = Math.max(res, sum);
            }
        } else {
            int sum = 0;
            for (int i = 0; i < n; i++) {
                sum += dataA[i] * dataB[i];
            }
            res = Math.max(res, sum);
        }
        return res;
    }


}
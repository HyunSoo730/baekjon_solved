import java.io.*;
import java.util.*;

class Solution
{
    public static void main(String args[]) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int T;
        T = Integer.parseInt(br.readLine());

        for(int test_case = 1; test_case <= T; test_case++)
        {
            n = Integer.parseInt(br.readLine());
            int[][] data = new int[n][n];

            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < n; j++) {
                    data[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            int[][] arr_90 = rotation(data);
            int[][] arr_180 = rotation(arr_90);
            int[][] arr_270 = rotation(arr_180);

            // 결과출력
            System.out.println("#" + test_case);
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    System.out.print(arr_90[i][j]);
                }
                System.out.print(" ");

                for (int j = 0; j < n; j++) {
                    System.out.print(arr_180[i][j]);
                }
                System.out.print(" ");

                for (int j = 0; j < n; j++) {
                    System.out.print(arr_270[i][j]);
                }
                System.out.println();
            }
        }
    }

    static int n;  // 배열 길이
    //시계 방향 90도 회전함수
    public static int[][] rotation(int[][] arr) {
        int[][] result = new int[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                result[i][j] = arr[n - 1 - j][i];
            }
        }
        return result;
    }
}
import java.io.*;
import java.util.StringTokenizer;

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
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());

            int max_sum = Integer.MIN_VALUE;
            int[][] data = new int[n][n];
            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < n; j++) {
                    data[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            //+형태
            int[] dx = {-1, 1, 0, 0};
            int[] dy = {0, 0, 1, -1};
            for (int x = 0; x < n; x++) {
                for (int y = 0; y < n; y++) {
                    int sum = data[x][y];
                    for (int len = 1; len < m; len++) {
                        for (int i = 0; i < 4; i++) {
                            int nx = x + dx[i] * len;
                            int ny = y + dy[i] * len;
                            if (nx >= 0 && nx < n && ny >= 0 && ny < n) {
                                sum += data[nx][ny];
                            }
                        }
                    }
                    if (sum > max_sum) {
                        max_sum = sum;
                    }
                }
            }

            //x 형태
            dx = new int[]{1, -1, 1, -1};
            dy = new int[]{-1, -1, 1, 1};
            for (int x = 0; x < n; x++) {
                for (int y = 0; y < n; y++) {
                    int sum = data[x][y];
                    for (int len = 1; len < m; len++) {
                        for (int i = 0; i < 4; i++) {
                            int nx = x + dx[i] * len;
                            int ny = y + dy[i] * len;
                            if (nx >= 0 && nx < n && ny >= 0 && ny < n) {
                                sum += data[nx][ny];
                            }
                        }
                    }
                    if (sum > max_sum) {
                        max_sum = sum;
                    }
                }
            }
            System.out.println("#" + test_case + " " + max_sum);
        }
    }
}
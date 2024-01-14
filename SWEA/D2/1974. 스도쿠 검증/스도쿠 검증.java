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
            int[][] data = new int[9][9];
            int res = 1;   // 애초에 세팅을 성공하는 값으로 세팅
            int flag = -1;
            for (int i = 0; i < 9; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < 9; j++) {
                    data[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            // 먼저 가로 세로에 대해서 진행
            for (int i = 0; i < 9; i++) {
                int rsum = 0;  // 열 합
                int csum = 0;  // 행 합
                for (int j = 0; j < 9; j++) {
                    rsum += data[i][j];
                    csum += data[j][i];
                }

                if (rsum != 45 || csum != 45) {
                    flag = 0;
                    res = 0;
                    break;
                }
            }
            if (flag == 0) {
                System.out.println("#" + test_case + " " + res);
                continue;
            }

            // 3x3 정사각형 구역 확인
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    int sum = 0;
                    for (int k = 0; k < 3; k++) {
                        for (int l = 0; l < 3; l++) {
                            sum += data[i*3 + k][j*3 + l];
                        }
                    }
                    if (sum != 45) {
                        flag = 0;
                        res = 0;
                        break;
                    }
                }
                if (flag == 0) {
                    break;
                }
            }
            System.out.println("#" + test_case + " " + res);
        }
    }
}
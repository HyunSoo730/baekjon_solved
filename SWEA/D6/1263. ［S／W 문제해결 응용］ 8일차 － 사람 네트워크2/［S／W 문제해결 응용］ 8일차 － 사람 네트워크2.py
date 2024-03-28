import java.awt.*;
import java.io.*;
import java.util.*;
import java.util.List;

public class Solution {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int T, INF = 1000000;
    static int[][] g;

    public static void main(String[] args) throws IOException {
        T = Integer.parseInt(br.readLine());
        for (int t = 1; t <= T; t++) {
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            g = new int[n][n];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    g[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if(g[i][j] == 0) g[i][j] = INF;
                    if(i==j) g[i][j] = 0; // ! 본인은 0
                }
            }

//            printBoard(g);
            for (int k = 0; k < n; k++) {
                for (int i = 0; i < n; i++) {
                    for (int j = 0; j < n; j++) {
                        g[i][j] = Math.min(g[i][k] + g[k][j], g[i][j]);
                    }
                }
            }

            // ! 모든 노드에 대한 최소 거리 계산
            int minSum = Integer.MAX_VALUE;
            for (int i = 0; i < n; i++) {
                int sum = 0;
                for (int j = 0; j < n; j++) {
                    sum += g[i][j];
                }
                minSum = Math.min(minSum, sum);
            }

            System.out.println("#" + t + " " + minSum);
        }


    }

    public static void printBoard(int[][] g){
        for (int i = 0; i < g.length; i++) {
            for (int j = 0; j < g[i].length; j++) {
                System.out.print(g[i][j] + " ");
            }
            System.out.println();
        }
    }

}
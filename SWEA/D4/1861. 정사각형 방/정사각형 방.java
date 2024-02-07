import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

    static int T, n;

    static int[][] g;
    static int roomNum, max_cnt;
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
    static int cnt, resX, resY;
    static boolean[][] visited;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        T = Integer.parseInt(br.readLine());
        for (int t = 1; t <= T; t++) {
            n = Integer.parseInt(br.readLine());
            g = new int[n][n];
            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < n; j++) {
                    g[i][j] = Integer.parseInt(st.nextToken());
                }
            }
            // 로직
            solve();
            System.out.println("#" + t + " " + roomNum + " " + max_cnt);
        }
    }

    public static void solve() {
        int res = 0;
        max_cnt = Integer.MIN_VALUE;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                visited = new boolean[n][n];
                visited[i][j] = true; // 시작 좌표 방문처리 후 시작.
                cnt = 0;
                DFS(i,j, 1);
                if(res < cnt){
                    res = cnt;
                    roomNum = g[i][j];
                    max_cnt = cnt;
                    resX = i;
                    resY = j;
                } else if (res == cnt && g[i][j] < g[resX][resY]) {
                    roomNum = g[i][j];
                    max_cnt = cnt;
                    resX = i;
                    resY = j;
                }
            }
        }

    }

    public static void DFS(int x, int y, int count) {
        cnt = Math.max(cnt, count);
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (isInner(nx, ny) && !visited[nx][ny]) {
                if (g[nx][ny] - g[x][y] == 1) {
                    visited[nx][ny] = true;
                    DFS(nx, ny, count + 1);
                    visited[nx][ny] = false;
                }
            }
        }
    }

    public static boolean isInner(int x, int y) {
        if (x < 0 || x > n - 1 || y < 0 || y > n - 1) {
            return false;
        }
        return true;
    }



    static class Point{
        int x, y;

        Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}
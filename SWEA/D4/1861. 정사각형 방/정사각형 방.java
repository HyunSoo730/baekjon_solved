import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

    static int T, n;
    static int[][] g;
    static int max_cnt, startRoom = Integer.MAX_VALUE;
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
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
            max_cnt = Integer.MIN_VALUE;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    DFS(i, j, 1, g[i][j]);
                }
            }
            System.out.println("#" + t + " " + startRoom + " " + max_cnt);
        }
    }

    // 현재 룸 넘버로 같이 그냥 저장용으로 넣어줌
    public static void DFS(int x, int y, int count, int roomNum) {
        if (count > max_cnt) {
            max_cnt = count;
            startRoom = roomNum;
        } else if (count == max_cnt) {
            startRoom = Math.min(roomNum, startRoom);
        }
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (isInner(nx, ny) && g[nx][ny] - g[x][y] == 1) {  // visited[][] 필요없음 ! 어차피 또 방문할 수가 없으니.
                DFS(nx, ny, count + 1, roomNum);
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
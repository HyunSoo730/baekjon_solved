import javax.xml.crypto.Data;
import java.awt.*;
import java.io.*;
import java.util.*;


public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    static int n,m,min_cnt;
    static int[][] g;
    static int[][] dis; // ! 벽 최소 제거 횟수.
    static int endX,endY, INF = 1000000;

    private static class Point{
        int x, y, cnt; // 벽을 부순 횟수

        Point(int x, int y, int cnt) {
            this.x = x;
            this.y = y;
            this.cnt = cnt;
        }
    }
    public static void main(String[] args) throws IOException {

        st = new StringTokenizer(br.readLine());
        m = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());
        g = new int[n][m];
        dis = new int[n][m];
        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            for (int j = 0; j < m; j++) {
                g[i][j] = line.charAt(j) - '0';
            }
        }

        for (int i = 0; i < n; i++) {
            Arrays.fill(dis[i], INF);
        }
        min_cnt = INF;
        endX = n-1;
        endY = m-1;

        BFS(0, 0);
        System.out.println(min_cnt);
    }

    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};

    public static boolean isInner(int x, int y) {
        if (x >= 0 && x < n && y >= 0 && y < m) {
            return true;
        }
        return false;
    }

    public static void BFS(int startX, int startY) {
        Deque<Point> dq = new ArrayDeque<>();
        dq.offer(new Point(startX, startY, 0));
        dis[startX][startY] = 0;
        while (!dq.isEmpty()) {
            Point now = dq.poll();
            if (now.x == endX && now.y == endY) {
                if (now.cnt < min_cnt) {
                    min_cnt = now.cnt;
                }
                continue; // ! 최단으로 확인해야 하므로
            }
            for (int i = 0; i < 4; i++) {
                int nx = now.x + dx[i];
                int ny = now.y + dy[i];
                if(!isInner(nx,ny)) continue;
                if (g[nx][ny] == 0) { // 이동 가능
                    if (now.cnt < dis[nx][ny]) {
                        dis[nx][ny] = now.cnt;
                        dq.offer(new Point(nx, ny, now.cnt));
                    }
                } else if (g[nx][ny] == 1) { // ! 벽.
                    if (now.cnt + 1 < dis[nx][ny]) {
                        dis[nx][ny] = now.cnt + 1;
                        dq.offer(new Point(nx, ny, now.cnt + 1));
                    }
                }
            }
        }
    }

}
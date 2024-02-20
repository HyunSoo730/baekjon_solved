import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {

    private static class Point{
        int x, y;

        Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
    static char red = 'R', green = 'G', blue = 'B';
    static int n;
    static char[][] g;
    static int cntA, cntB, cnt;
    static boolean[][] visited;
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        g = new char[n][n];
        for (int i = 0; i < n; i++) {
            String data = br.readLine();
            for (int j = 0; j < n; j++) {
                g[i][j] = data.charAt(j);
            }
        }
        visited = new boolean[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (!visited[i][j]) {
                    BFS(i, j, g[i][j]);
                    cnt += 1;
                }
            }
        }
        cntA = cnt;
        cnt = 0;
        visited = new boolean[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if(g[i][j] == red) g[i][j] = green;
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (!visited[i][j]) {
                    BFS(i, j, g[i][j]);
                    cnt += 1;
                }
            }
        }
        cntB = cnt;
        System.out.println(cntA);
        System.out.println(cntB);
    }

    public static void BFS(int a, int b, char color) {
        Deque<Point> dq = new ArrayDeque<>();
        visited[a][b] = true;  // 시작점 방문처리
        dq.offer(new Point(a, b));  // 시작점 큐에 넣어두고 시작

        while (!dq.isEmpty()) {
            Point now = dq.poll();
            for (int i = 0; i < 4; i++) {
                int nx = now.x + dx[i];
                int ny = now.y + dy[i];
                if (isInner(nx, ny) && g[nx][ny] == color && !visited[nx][ny]) {
                    visited[nx][ny] = true;  // 방문처리 후
                    dq.offer(new Point(nx, ny));
                }
            }
        }
    }

    public static boolean isInner(int x, int y) {
        if (x >= 0 && x < n && y >= 0 && y < n) {
            return true;
        }
        return false;
    }
}
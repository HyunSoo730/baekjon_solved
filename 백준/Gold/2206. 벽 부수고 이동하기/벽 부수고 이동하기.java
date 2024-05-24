import java.io.*;
import java.util.*;


public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    static int n,m, endX,endY, min_dis;
    static int[][] g; // ! 그래프
    static int[][][] dis;
    static int INF = 10000000;

    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};
    private static class Point{
        int x,y,dis,cnt; // ! 현재 좌표, 거리, 벽을 부쉈는지 체크

        Point(int x, int y, int dis, int cnt) {
            this.x = x;
            this.y = y;
            this.dis = dis;
            this.cnt = cnt;
        }
    }

    public static void main(String[] args) throws IOException {

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        g = new int[n][m];
        dis = new int[n][m][2]; // ! 벽을 안부쉈음 0 벽을 부쉈음 1
        // ! 즉 dis[x][y][0] , dis[x][y][1] 벽을 부쉈을 때의 최단거리, 아닐 때의 최단거리 등등. 계산 가능.
        endX = n-1;
        endY = m-1;
        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            for (int j = 0; j < m; j++) {
                g[i][j] = line.charAt(j) - '0'; // 인트로 변환
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                Arrays.fill(dis[i][j], INF);
            }
        }

        min_dis = INF;
        BFS(0, 0);
        if (min_dis == INF) {
            System.out.println(-1);
        } else {
            System.out.println(min_dis);
        }

    }

    public static boolean isInner(int x, int y) {
        if (x >= 0 && x < n && y >= 0 && y < m) {
            return true;
        }
        return false;
    }

    public static void BFS(int startX, int startY) {
        Deque<Point> dq = new ArrayDeque<>();
        dq.offer(new Point(startX, startY, 1, 0)); // ! 시작 좌표 포함
        dis[startX][startY][0] = 1; // ! 시작좌표 세팅.

        while (!dq.isEmpty()) {
            Point now = dq.poll();
            if (now.x == endX && now.y == endY) {
                if (now.dis < min_dis) {
                    min_dis = now.dis;
                    break; // ! 도착점에서 다시 할 필요 없음.
                }
            }

            for (int i = 0; i < 4; i++) {
                int nx = now.x + dx[i];
                int ny = now.y + dy[i];
                if(!isInner(nx,ny)) continue; // ! 좌표 내부이면 continue

                if (g[nx][ny] == 0) { // ! 이동 가능
                    if (now.dis + 1 < dis[nx][ny][now.cnt]) {
                        dis[nx][ny][now.cnt] = now.dis + 1;
                        dq.offer(new Point(nx, ny, now.dis + 1, now.cnt));
                    }
                } else if (g[nx][ny] == 1) { // ! 벽
                    if (now.cnt == 0) { // ! 벽을 부순 적이 없다면.
                        if (now.dis + 1 < dis[nx][ny][1]) { // ! 벽을 부쉈을 때보다 작으면
                            dis[nx][ny][1] = now.dis + 1;
                            dq.offer(new Point(nx, ny, now.dis + 1, 1));
                        }
                    }
                }
            }
        }
    }

    public static void 보드출력(int[][] g) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                System.out.print(g[i][j] + " ");
            }
            System.out.println();
        }
    }

}
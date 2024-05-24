import javax.xml.crypto.Data;
import java.awt.*;
import java.io.*;
import java.util.*;


public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    static int n,m,k;  // ! k는 벽을 부술 수 있는 최대 횟수
    static int[][] g;
    static int[][][] dis;
    static int endX,endY;
    static int INF = 1000000, min_dis;

    private static class Data{
        int x, y, dis, cnt;

        Data(int x, int y, int dis, int cnt) {
            this.x = x;
            this.y = y;
            this.dis = dis;
            this.cnt = cnt;
        }
    }

    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};

    public static boolean isInner(int x, int y) {
        return x >= 0 && x < n && y >= 0 && y < m;
    }

    public static void main(String[] args) throws IOException {

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        g = new int[n][m];
        dis = new int[n][m][k+1];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                Arrays.fill(dis[i][j], INF);
            }
        }

        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            for (int j = 0; j < m; j++) {
                g[i][j] = line.charAt(j) - '0';
            }
        }
        endX = n-1; endY = m-1;
        min_dis = INF;
        BFS(0, 0);
        if (min_dis == INF) {
            System.out.println(-1);
        } else {
            System.out.println(min_dis);
        }

    }

    public static void BFS(int startX, int startY) {
        Deque<Data> dq = new ArrayDeque<>();
        dq.offer(new Data(startX, startY, 1, 0));

        while (!dq.isEmpty()) {
            Data now = dq.poll();
            if (now.x == endX && now.y == endY) {
                min_dis = now.dis;
                break;
            }
            for (int i = 0; i < 4; i++) {
                int nx = now.x + dx[i];
                int ny = now.y + dy[i];
                if(!isInner(nx,ny)) continue;

                if (g[nx][ny] == 0) { // ! 이동 가능
                    if (now.dis + 1 < dis[nx][ny][now.cnt]) {
                        dis[nx][ny][now.cnt] = now.dis + 1; // ! 갱신
                        dq.offer(new Data(nx, ny, now.dis + 1, now.cnt)); // ! 갱신 됐으니 다시 해당 지점에서 시작
                    }
                } else if (g[nx][ny] == 1) { // ! 벽인 경우
                    if (now.cnt < k) { // ! 벽을 더 깰 수 있다면
                        if (now.dis + 1 < dis[nx][ny][now.cnt + 1]) {
                            dis[nx][ny][now.cnt + 1] = now.dis + 1;
                            dq.offer(new Data(nx, ny, now.dis + 1, now.cnt + 1));
                        }
                    }
                }
            }
        }
    }

}
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.StringTokenizer;
import java.util.function.IntFunction;

public class Main {

    // ! 말이 되고픈 원숭이
    // ! 원숭이 : 상하좌우 움직임
    // ! 말 : 나이트 움직임
    // ! 총 k번만 이동 가능. 그 외에는 인접한 칸으로만 움직임 가능
    // ! 격자판의 맨 왼쪽 위에서 맨 오른쪽 아래까지 이동. - > 최단거리
    // ! 0은 이동 가능, 1은 이동 불가.
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    static int n, m, k; // ! k는 말처럼 이동 가능 횟수
    static int[][] g;
    static int[][][] dis; // ! 최단 거리 기록용 배열
    static int endX,endY,INF = 10000000;
    static int MIN_DIS;

    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};
    static int[] hx = {-2, -1, 1, 2, 2, 1, -1, -2};
    static int[] hy = {1, 2, 2, 1, -1, -2, -2, -1};

    private static class Data {

        int x, y, dis, cnt;

        Data(int x, int y, int dis, int cnt) {
            this.x = x;
            this.y = y;
            this.dis = dis;
            this.cnt = cnt;
        }
    }

    public static boolean isInner(int x, int y){
        return x >= 0 && x < n && y >= 0 && y < m;
    }

    public static void main(String[] args) throws Exception {
        st = new StringTokenizer(br.readLine());
        k = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        m = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());

        g = new int[n][m];
        MIN_DIS = INF;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                g[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        dis = new int[n][m][k+1]; // ! k번까지 가능
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                Arrays.fill(dis[i][j], INF);
            }
        }

        endX = n-1;
        endY = m-1;
        BFS(0,0);
        if (MIN_DIS == INF) {
            System.out.println(-1);
        } else {
            System.out.println(MIN_DIS);
        }
    }

    public static void BFS(int startX,int startY) {
        Deque<Data> dq = new ArrayDeque<>();
        dq.offer(new Data(startX, startY, 0, 0));
        dis[startX][startY][0] = 0; // ! 최단거리 기록하고 시작

        while (!dq.isEmpty()) {
            Data now = dq.poll();
            if (now.x == endX && now.y == endY) {
                MIN_DIS = Math.min(MIN_DIS, now.dis);
                continue;
            }

            // ! 원숭이 움직임 먼저
            for (int i = 0; i < 4; i++) {
                int nx = now.x + dx[i];
                int ny = now.y + dy[i];
                if(!isInner(nx,ny)) // ! 외부 좌표라면 패스
                    continue;

                if (g[nx][ny] == 0) {
                    if (now.dis + 1 < dis[nx][ny][now.cnt]) {
                        dis[nx][ny][now.cnt] = now.dis + 1;
                        dq.offer(new Data(nx, ny, now.dis + 1, now.cnt));
                    }
                }
            }

            // ! 말 움직임 먼저
            for (int i = 0; i < 8; i++) {
                int nx = now.x + hx[i];
                int ny = now.y + hy[i];
                if(!isInner(nx,ny))
                    continue;

                if (g[nx][ny] == 0 && now.cnt < k) {
                    if(now.dis + 1 < dis[nx][ny][now.cnt + 1]){
                        dis[nx][ny][now.cnt + 1] = now.dis + 1;
                        dq.offer(new Data(nx, ny, now.dis + 1, now.cnt + 1));
                    }
                }
            }
        }
    }
}
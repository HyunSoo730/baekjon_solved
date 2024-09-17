import java.io.IOException;
import java.io.*;
import java.util.*;

public class Main {

    // ! N*M 보드
    // ! 맵에서 0은 이동 가능, 1은 벽
    // ! (1,1) -> (N,M) 이동. 최단경로
    // ! 벽 부수고 최대 K개까지 부수고 이동 가능

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    static int n,m,k; // ! k는 벽을 부술 수 있는 횟수
    static int[][] g;
    static int[][][] dis;
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};
    static int endX,endY, INF = 10000000;
    static int MIN_DIS = INF;

    private static class Data {
        int x,y,dis,cnt;

        Data(int x, int y, int dis, int cnt) {
            this.x = x;
            this.y = y;
            this.dis = dis;
            this.cnt = cnt;
        }
    }

    public static boolean isInner(int x, int y) {
        return x >= 0 && x < n && y >= 0 && y < m;
    }

    public static void main(String[] args) throws IOException {

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        g = new int[n][m];
        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            for (int j = 0; j < m; j++) {
                g[i][j] = line.charAt(j) - '0';
            }
        }

        // ! 최단거리 기록하는 dis에 최댓값으로 채워넣기
        dis = new int[n][m][k+1]; // ! 최대 k번
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                Arrays.fill(dis[i][j], INF);
            }
        }
        endX = n-1;
        endY = m-1;

        BFS(0, 0);
        if (MIN_DIS == INF) {
            System.out.println(-1);
        } else {
            System.out.println(MIN_DIS);
        }
    }

    public static void BFS(int startX, int startY) {
        Deque<Data> dq = new ArrayDeque<>();
        dq.offer(new Data(startX, startY, 1, 0)); // ! 시작지점 포함
        dis[startX][startY][0] = 0; // ! 시작지점 세팅

        while (!dq.isEmpty()) {
            Data now = dq.poll(); // ! 맨 앞에 꺼내서 확인
            if (now.x == endX && now.y == endY) {
                MIN_DIS = Math.min(MIN_DIS, now.dis);
            }
            for (int i = 0; i < 4; i++) {
                int nx = now.x + dx[i];
                int ny = now.y + dy[i];
                // ! 이동이 가능하면서, 최단거리일 때 진행
                if (!isInner(nx, ny))
                    continue;

                if (g[nx][ny] == 0) { // ! 이동 가능한 위치
                    if (now.dis + 1 < dis[nx][ny][now.cnt]) { // ! 최단거리 갱신 가능
                        dis[nx][ny][now.cnt] = now.dis + 1;
                        dq.offer(new Data(nx, ny, now.dis + 1, now.cnt));
                    }
                }else{ // ! 이동 못하더라도 벽 부수고 갈 수 있는지 확인
                    if (now.cnt < k) {
                        if (now.dis + 1 < dis[nx][ny][now.cnt + 1]) {
                            dis[nx][ny][now.cnt+1] = now.dis + 1;
                            dq.offer(new Data(nx, ny, now.dis + 1, now.cnt + 1));
                        }
                    }
                }
            }
        }



    }

}
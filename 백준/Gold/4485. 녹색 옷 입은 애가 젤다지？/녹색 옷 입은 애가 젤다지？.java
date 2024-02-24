import org.w3c.dom.Node;

import java.awt.*;
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    static int n;
    static int[][] g;
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
    static int[][] dis;  // ! 최단거리 비용 기록용

    private static class Point implements Comparable<Point> {
        int x, y;
        int distance;

        Point(int x, int y, int distance) {
            this.x = x;
            this.y = y;
            this.distance = distance;
        }

        @Override
        public int compareTo(Point point) {
            return this.distance - point.distance;
        }
    }

    public static void main(String[] args) throws IOException {

        int cnt = 1;
        while (true) {
            n = Integer.parseInt(br.readLine());
            if(n == 0) break;
            g = new int[n][n];
            dis = new int[n][n];  // ! 최단거리 기록
            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < n; j++) {
                    g[i][j] = Integer.parseInt(st.nextToken());
                    dis[i][j] = Integer.MAX_VALUE;
                }
            }
            // ! 일단 dis배열을 맥스로 모두 채움

            dijkstra();
            System.out.println("Problem " + cnt++ + ": " + dis[n - 1][n - 1]);
        }
    }

    public static void dijkstra() {
        PriorityQueue<Point> pq = new PriorityQueue<>();
        dis[0][0] = g[0][0]; // ! 초기값 세팅 -> dis는 시작점 0,0에서 해당 좌표까지 가는데 드는 비용의 최소값
        pq.offer(new Point(0, 0, g[0][0]));  // 초기값 세팅

        while (!pq.isEmpty()) {
            Point now = pq.poll();
            // 해당 좌표로부터 4방 탐색 진행
            for (int i = 0; i < 4; i++) {
                int nx = now.x + dx[i];
                int ny = now.y + dy[i];

                if(!isInner(nx,ny)) continue;  // !좌표 벗어나면 안돼
                if (dis[now.x][now.y] + g[nx][ny] < dis[nx][ny]) { // ! 기존의 가중치보다 작은 경우
                    dis[nx][ny] = dis[now.x][now.y] + g[nx][ny]; // ! 가중치 갱신
                    pq.offer(new Point(nx, ny, dis[nx][ny]));
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
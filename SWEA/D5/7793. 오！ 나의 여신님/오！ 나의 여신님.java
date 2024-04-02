import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.StringTokenizer;


public class Solution {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    static int T,n,m,INF = 10000000;
    static char[][] g;
    static int[][] dis, devils;
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};
    static char des = 'D', wall = 'X', blank = '.', devil = '*'; // ! 도착점, 벽, 빈칸
    static int startX,startY,endX,endY;
    private static class Point{
        int x,y,t;

        Point(int x, int y, int t) {
            this.x = x;
            this.y = y;
            this.t = t;
        }
    }
    public static boolean isInner(int x, int y) {
        return (x >= 0 && x < n && y >= 0 && y < m);
    }
    public static void step1() { // ! 악마가 도착하는 시간을 기록
        Deque<Point> dq = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (g[i][j] == devil) {
                    dq.offer(new Point(i,j,0));
                }
            }
        }

        while (!dq.isEmpty()) {
            Point now = dq.poll();
            for (int i = 0; i < 4; i++) {
                int nx = now.x + dx[i];
                int ny = now.y + dy[i];
                if (isInner(nx, ny) && g[nx][ny] == blank) { // ! 악마가 이동 가능
                    if(now.t+1 < devils[nx][ny]){
                        devils[nx][ny] = now.t + 1;
                        dq.offer(new Point(nx, ny, now.t + 1));
                    }
                }
            }
        }
    }

    public static void step2(int a, int b) { // ! step2 : 악마가 도착한 시간을 바탕으로 수연이가 갈 수 있는지 : 최단시간 갱신
        Deque<Point> dq = new ArrayDeque<>();
        dq.offer(new Point(a, b, 0)); // ! 현재 경로의 시간과 함께
        while (!dq.isEmpty()) {
            Point now = dq.poll();
            int x = now.x;
            int y = now.y;
            int t = now.t;
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (isInner(nx, ny) && g[nx][ny] == blank) { // ! 일단 이동 가능해
                    if (t + 1 < devils[nx][ny]) { // ! 이동할 좌표까지의 시간이 악마가 도달할 시간보다 작아야만 이동 가능
                        if (t + 1 < dis[nx][ny]) { // ! 또한 기존의 최단시간보다 작아야만
                            dis[nx][ny] = t + 1;
                            dq.offer(new Point(nx, ny, t + 1));
                        }
                    }
                } else if (isInner(nx, ny) && g[nx][ny] == des) { // ! 도착점인 경우 갱신만 진행
                    if (t + 1 < dis[nx][ny]) {
                        dis[nx][ny] = t + 1;
                    }
                }
            }
        }
    }

    public static void printBoard(int[][] g) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                System.out.print(g[i][j] + " ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) throws IOException {
        T = Integer.parseInt(br.readLine());
        for (int t = 1; t <= T; t++) {
            st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());
            g = new char[n][m];

            // ! 보드 입력
            for (int i = 0; i < n; i++) {
                String data = br.readLine();
                for (int j = 0; j < m; j++) {
                    g[i][j] = data.charAt(j);
                    if (g[i][j] == 'S') { // ! 시작점
                        startX = i;
                        startY = j;
                        g[i][j] = blank;
                    }
                    if (g[i][j] == des) { // ! 도착점
                        endX = i;
                        endY = j;
                    }
                }
            }

            dis = new int[n][m];
            devils = new int[n][m];
            for (int i = 0; i < n; i++) {
                Arrays.fill(dis[i], INF);
                Arrays.fill(devils[i], INF);
            }

            step1();
//            printBoard(devils);
            step2(startX, startY);

//            printBoard(dis);
            if (dis[endX][endY] == INF) {
                System.out.println("#" + t + " " + "GAME OVER");
            } else {
                System.out.println("#" + t + " " + dis[endX][endY]);
            }
        }
    }


}
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    private static class Point{
        int x, y;

        Point(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public String toString() {
            return "x : " + x + " y : " + y;
        }
    }

    static int n, m, max;
    static int[][] g, temp;
    static List<Point> data = new ArrayList<>();
    static Deque<Point> dq = new ArrayDeque<>();
    static int size, wall = 1;
    static int[] select;
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        g = new int[n][m];
        temp = new int[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                g[i][j] = Integer.parseInt(st.nextToken());
                if(g[i][j] == 0) data.add(new Point(i, j));
            }
        }
//        printArray(g);
//        for (Point p : dq) {
//            System.out.println(p);
//        }
        size = data.size();
        select = new int[3];  // ! 선택한 자리들의 인덱스
        DFS(0, 0);
        System.out.println(max);
    }

    public static void installWall(int[][] g) {  // ! 벽 설치
//        System.out.print("설치한 좌표 : ");
        for (int i = 0; i < 3; i++) {
            int index = select[i];
            Point p = data.get(index);
//            System.out.print("(" + p.x + ", " + p.y + "),  ");
            g[p.x][p.y] = wall;  // 해당 좌표 벽 설치
        }
//        System.out.println();
    }

    public static void copyWall() {
        temp = new int[n][m];
        for (int i = 0; i < n; i++) {
            temp[i] = Arrays.copyOf(g[i], g[i].length);
        }
    }

    public static boolean isInner(int x, int y) {
        if (x >= 0 && x < n && y >= 0 && y < m) {
            return true;
        }
        return false;
    }

    public static void BFS(int[][] g) {
        dq = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if(g[i][j] == 2) dq.offer(new Point(i, j));
            }
        }
        // ! 매 순간마다 dq를 초기화해줬어야 헀음.
        while (!dq.isEmpty()) {
            Point now = dq.poll();
            for (int i = 0; i < 4; i++) {
                int nx = now.x + dx[i];
                int ny = now.y + dy[i];
                if (isInner(nx, ny)  && g[nx][ny] == 0) {  // ! 방문전이면서
                    g[nx][ny] = 2;
                    dq.offer(new Point(nx, ny));
                }
            }
        }
    }

    public static void printArray(int[][] g){
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                System.out.print(g[i][j] + " ");
            }
            System.out.println();
        }
    }
    public static int countSafeZone(int[][] g) {
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if(g[i][j] == 0) cnt += 1;
            }
        }
        return cnt;
    }

    public static void DFS(int start, int L) {
        if (L == 3) { // ! 3개 모두 선택
            // 원본 g에 복사 후 벽 설치
//            printArray(g);
            copyWall();
            installWall(temp);  // ! 임시 벽에 벽 설치
//            System.out.println("벽 설치 후 좌표");
//            printArray(temp);
//            System.out.println("===============");
            BFS(temp);
            int cnt = countSafeZone(temp);
//            System.out.println("현재 설치했을 때의 개수 : " + cnt);
            max = Math.max(max, cnt);

        } else {
            for (int i = start; i < size; i++) {
                select[L] = i;
                DFS(i + 1, L + 1);
            }
        }
    }
}
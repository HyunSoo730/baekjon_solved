import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

class Point {
    int x, y;

    Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

}

public class Main {

    static int n, m;
    static int[][] g;
    static int cnt, time, res;
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
    static boolean[][] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        g = new int[n][m];
        visited = new boolean[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                g[i][j] = Integer.parseInt(st.nextToken());
                if (g[i][j] == 1) cnt += 1;  // 치즈 개수 증가시키기
            }
        }

        BFS(0, 0);
        System.out.println(time);
        System.out.println(res);
    }

    public static void BFS(int x, int y) {
        visited[x][y] = true;  // 시작점 방문처리
        Deque<Point> dq = new ArrayDeque<>();
        dq.offer(new Point(x, y));

        int meltCnt = 0;
        time += 1;
        while (!dq.isEmpty()) {
            Point now = dq.poll();
            for (int i = 0; i < 4; i++) {
                int nx = now.x + dx[i];
                int ny = now.y + dy[i];
                if (isInner(nx, ny) && !visited[nx][ny]) {
                    if (g[nx][ny] == 1) {   // 치즈 녹여야함
                        visited[nx][ny] = true;
                        g[nx][ny] = 0;
                        meltCnt += 1;  // 녹인 개수 증가
                    } else if (g[nx][ny] == 0) {   // 치즈 없는 곳이면 치즈를 찾기 위해 반복
                        visited[nx][ny] = true;
                        dq.offer(new Point(nx, ny));
                    }
                }
            }
        }
        cnt -= meltCnt;  // 매 횟수마다 녹인 개수 빼줘
        if (cnt == 0) {  // 다 녹인 경우
            res = meltCnt;   // 다 녹였을 때의 마지막 개수 저장
        } else {
            visited = new boolean[n][m];
            BFS(0, 0);  // 다시 탐색 진행
        }
    }

    public static boolean isInner(int x, int y) {
        if (x >= 0 && x < n && y >= 0 && y < m) {
            return true;
        }
        return false;
    }
}
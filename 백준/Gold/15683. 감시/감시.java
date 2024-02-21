import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    static int n, m, minCnt = Integer.MAX_VALUE;
    static int[][] g, copy;
    static boolean[][] visited;
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};  // 위, 오른쪽, 아래, 왼쪽
    static int wall = 6, watch = -1, size;  // 벽
    static List<CCTV> data = new ArrayList<>();
    static int[] direction;

    private static class CCTV {
        int num;
        int x, y;

        CCTV(int num, int x, int y) {
            this.num = num;
            this.x = x;
            this.y = y;
        }
    }

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        g = new int[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                g[i][j] = Integer.parseInt(st.nextToken());
                if (g[i][j] != 0 && g[i][j] != wall) {
                    data.add(new CCTV(g[i][j], i, j));
                }
            }
        }
        size = data.size();
        direction = new int[size];

        DFS(0);
        System.out.println(minCnt);
    }

    public static void DFS(int L) {
        if (L == size) {
            // 해당 CCTV 별로 어떤 방향으로 할 지 정함.
            copy(g);
            for (int i = 0; i < size; i++) {
                solve(data.get(i), direction[i]);
            }
            int cnt = 0;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (copy[i][j] == 0) {
                        cnt += 1;
                    }
                }
            }
            minCnt = Math.min(minCnt, cnt);

        } else {
            for (int i = 0; i < 4; i++) {
                direction[L] = i; // 각 CCTV 별로 모든 조합을 확인해야 함.
                DFS(L + 1);
            }
        }
    }

    public static void solve(CCTV cctv, int d) {
        if (cctv.num == 1) {
            BFS(cctv, d);
        } else if (cctv.num == 2) {
            if (d == 0 || d == 2) {
                BFS(cctv, 0);
                BFS(cctv, 2);
            } else {
                BFS(cctv, 1);
                BFS(cctv, 3);
            }
        } else if (cctv.num == 3) {
            if (d == 0) {
                BFS(cctv, 0);
                BFS(cctv, 1);
            } else if (d == 1) {
                BFS(cctv, 1);
                BFS(cctv, 2);
            } else if (d == 2) {
                BFS(cctv, 2);
                BFS(cctv, 3);
            } else if (d == 3) {
                BFS(cctv, 3);
                BFS(cctv, 0);
            }
        } else if (cctv.num == 4) {
            if (d == 0) {
                BFS(cctv,0);
                BFS(cctv,1);
                BFS(cctv,2);
            } else if (d == 1) {
                BFS(cctv,1);
                BFS(cctv,2);
                BFS(cctv,3);
            } else if (d == 2) {
                BFS(cctv, 2);
                BFS(cctv, 3);
                BFS(cctv, 0);
            } else if (d == 3) {
                BFS(cctv,3);
                BFS(cctv,0);
                BFS(cctv,1);
            }
        } else if (cctv.num == 5) {
            BFS(cctv, 0);
            BFS(cctv, 1);
            BFS(cctv, 2);
            BFS(cctv, 3);
        }
    }

    public static void BFS(CCTV cctv, int d) {
        Deque<CCTV> dq = new ArrayDeque<>();
        boolean[][] visited = new boolean[n][m];
        visited[cctv.x][cctv.y] = true;
        dq.offer(cctv);
        while (!dq.isEmpty()) {
            CCTV now = dq.poll();
            int nx = now.x + dx[d];
            int ny = now.y + dy[d];
            if (isInner(nx, ny) && copy[nx][ny] != wall && !visited[nx][ny]) {
                if (copy[nx][ny] == 0) {  // 아직 감시 점 방문 안함
                    visited[nx][ny] = true;
                    copy[nx][ny] = watch;   // 방문처리 후 감시 당하는 지점이라고 표시
                    dq.offer(new CCTV(cctv.num, nx, ny));
                } else {  // 다른 cctv나 감시 대상점이라면
                    dq.offer(new CCTV(cctv.num, nx, ny));  // 그냥 넣어주고 끝.
                }
            }
        }

    }

    public static void copy(int[][] src) {
        copy = new int[src.length][];
        for (int i = 0; i < src.length; i++) {
            copy[i] = Arrays.copyOf(src[i], src[i].length);
        }
    }

    public static boolean isInner(int x, int y) {
        if (x >= 0 && x < n && y >= 0 && y < m) {
            return true;
        }
        return false;
    }

}
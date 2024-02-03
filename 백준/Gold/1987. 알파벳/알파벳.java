import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.sql.SQLOutput;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;


public class Main {
    static StringTokenizer st;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    static int n, m, res = Integer.MIN_VALUE;
    static char[][] g;
    static boolean[][] visited;
    static Set<Character> set = new HashSet<>();
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
    public static void main(String[] args) throws Exception {
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        g = new char[n][m];
        for (int i = 0; i < n; i++) {
            String temp = br.readLine();
            for (int j = 0; j < m; j++) {
                g[i][j] = temp.charAt(j);
            }
        }

        visited = new boolean[n][m];
        DFS(0, 0, 1);
        System.out.println(res);
    }

    public static void DFS(int x, int y, int cnt) {
        // 현재 위치 최대 칸인지 갱신
        visited[x][y] = true;
        set.add(g[x][y]);  
        // 시작 위치 방문 처리 및 알파벳 갱신
        res = Math.max(res, cnt);

        // 내가 할 일 : 현재 위치로부터 4방 탐색(방문X, 좌표 유효, 처음 만나는 알파벳)
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (isInner(nx, ny) && !visited[nx][ny]) { // 좌표가 유효하면서, 아직 방문 전.
                if(!set.contains(g[nx][ny])){ // 존재하지 않으면 깊이 들어감
                    visited[nx][ny] = true;
                    set.add(g[nx][ny]);
                    DFS(nx,ny,cnt+1);
                    visited[nx][ny] = false;
                    set.remove(g[nx][ny]);
                }
            }
        }
    }

    public static boolean isInner(int x, int y) {
        if (x < 0 || x > n - 1 || y < 0 || y > m - 1) {
            return false;
        }
        return true;
    }

}
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Main {

    static int n, m;
    static int[][] visited;
    static char[][] chars;
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
    static int cnt;
    static int visitedId = 1;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        chars = new char[n][m];
        visited = new int[n][m];
        for (int i = 0; i < n; i++) {
            String word = br.readLine();
            for (int j = 0; j < m; j++) {
                chars[i][j] = word.charAt(j);
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (visited[i][j] == 0) {
                    DFS(i, j, visitedId++);
                }
            }
        }
        System.out.println(cnt);

    }

    public static void DFS(int x, int y, int visitedId) {
        if (visited[x][y] != 0) {  // 이미 방문한 경험이 있음
            if (visited[x][y] == visitedId) {  // 사이클 형성
                cnt += 1;
            }
        } else {  // 방문한 적이 없다면 방문처리 후 계속 들어가
            visited[x][y] = visitedId;
            int dir = direction(chars[x][y]);
            int nx = x + dx[dir];
            int ny = y + dy[dir];
            DFS(nx, ny, visitedId);
        }
    }

    public static int direction(char c) {
        switch (c) {
            case 'D':
                return 0;
            case 'U':
                return 1;
            case 'R':
                return 2;
            case 'L':
                return 3;
        }
        return -1;
    }
}
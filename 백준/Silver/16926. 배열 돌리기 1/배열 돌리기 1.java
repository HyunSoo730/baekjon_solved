import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static int n,m, r;  // 배열 크기 NxM 회전 수 r
    static int min;  // 가로 세로 중 작은 값 저장
    static int[][] g;
    static int[] dx = {0, 1, 0, -1};  // 왼쪽으로 넣는, 위로 넣는, 오른쪽으로 넣는, 아래로 넣는
    static int[] dy = {1, 0, -1, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken()); // 가로
        m = Integer.parseInt(st.nextToken()); // 세로
        r = Integer.parseInt(st.nextToken()); // 회전수
        g = new int[n][m];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                g[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        min = Math.min(n, m);  /// 행, 열 중 더 작은 값 구함.

        for (int i = 0; i < r; i++) {
            rotate();
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                System.out.print(g[i][j] + " ");
            }
            System.out.println();
        }
    }

    // 회전 시키는 메소드
    public static void rotate() {  // 칸별 반시계 회전
        for (int i = 0; i < min / 2; i++) {  // 회전 시킬 그룹의 갯수
            int x = i;
            int y = i;
            int temp = g[x][y];  //  마지막에 넣을 값 미리 빼놓음

            int idx = 0;  //
            while (idx < 4) {  // 왼쪽으로 넣는, 위로 넣는, 오른쪽으로 넣는, 아래로 넣는
                int nx = x + dx[idx];
                int ny = y + dy[idx];

                // 좌표 유효하다면
                if (isInner(nx, ny, i)) {
                    g[x][y] = g[nx][ny];
                    x = nx;
                    y = ny;
                } else {  // 범위를 벗어났다면 다음 방향으로 넘어감
                    idx += 1;
                }
            }
            g[i+1][i] = temp;  // 빼 놓은 값 넣어준다.
        }
    }

    public static boolean isInner(int x, int y, int L) {
        if (x < L || x > n - L - 1 || y < L || y > m - L - 1) {
            return false;
        }
        return true;
    }
}
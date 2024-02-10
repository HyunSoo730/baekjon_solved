import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int n,m,r;
    static int rot_time;
    static int[][] arr;
    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {1, 0, -1, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken()); // 행 크기
        m = Integer.parseInt(st.nextToken()); // 열 크기
        r = Integer.parseInt(st.nextToken()); // 회전 횟수

        arr = new int[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        rot_time = Math.min(n, m)/2;  // 행, 열 중 더 작은 값 / 2

        for (int i = 0; i < r; i++) {
            반시계_한칸회전();  // 회전 횟수만큼 한 칸씩 반시계 회전
        }

        printArray();
    }


    public static void 반시계_한칸회전() {
        for (int layer = 0; layer < rot_time; layer++) {
            int x = layer;
            int y = layer;
            int temp = arr[x][y]; // 저장 값

            for (int dir = 0; dir < 4; dir++) {
                while(true){
                    int nx = x + dx[dir];
                    int ny = y + dy[dir];

                    if (isInner(nx, ny, layer)) {
                        arr[x][y] = arr[nx][ny];
                        x = nx;
                        y = ny;
                    } else {
                        break;
                    }
                }
            }
            arr[x+1][y] = temp; // 처음 값은 다시 넣어줘야지
        }
    }

    public static boolean isInner(int x, int y, int layer) {
        if (x >= layer && x < n - layer && y >= layer && y < m - layer) {
            return true;
        }
        return false;
    }

    public static void printArray() {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
    }
}
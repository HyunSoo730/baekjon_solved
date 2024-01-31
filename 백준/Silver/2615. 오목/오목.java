import java.io.FileInputStream;
import java.util.Scanner;
import java.util.StringTokenizer;

/**
 * @author 조현수
 * @date 24.01.29
 * @link https://www.acmicpc.net/problem/2615
 * @keyword_solution 완전탐색, 현재 위치로부터 4개의 방향 탐색하면서 내려가기
 * 1. 바둑알 정보를 체크해서 승자 확인 또는 아직 결정되지 않았는지 확인
 * 1-1. 둘이 동시에 이기거나 두 군데 이상에서 이기는 경우는 X
 * 2. 5목 (6목 X) -> 제한사항 체크
 * 3. 출력할 때 가장 왼쪽 위의 시작좌표를 출력 -> 순차적으로 내려가야겠다고 생각
 * @input 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 * 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 * 0 1 2 0 0 2 2 2 1 0 0 0 0 0 0 0 0 0 0
 * 0 0 1 2 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0
 * 0 0 0 1 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 * 0 0 0 0 1 2 2 0 0 0 0 0 0 0 0 0 0 0 0
 * 0 0 1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0
 * 0 0 0 0 0 0 2 1 0 0 0 0 0 0 0 0 0 0 0
 * 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 * 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 * 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 * 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 * 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 * 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 * 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 * 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 * 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 * 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 * 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 * @output 1
 * 3 2
 * @time_complex O(N ^ 2)
 * @perf 메모리 19220	시간 272
 */
public class Main {

    static int[][] data = new int[20][20];
    static int startX, startY;
    static int winColor;
    static int dx[] = {0, 1, 1, -1};
    static int dy[] = {1, 0, 1, 1};
    static StringTokenizer st;
    public static void main(String[] args) throws Exception {
        // 여기에 코드를 작성하세요.
        Scanner sc = new Scanner(System.in);

        for (int i = 1; i <= 19; i++) {
            for (int j = 1; j <= 19; j++) {
                data[i][j] = sc.nextInt();
            }
        }

        boolean flag = false;  // 경기를 누군가가 이겼다면 true, 아니면 false 유지
        outer:
        for (int i = 1; i <= 19; i++) {
            for (int j = 1; j <= 19; j++) {
                // 현재 좌표에서 검사 진행
                if (data[i][j] == 1) {
                    for (int d = 0; d < 4; d++) {
                        if (BFS(i, j, 1, d)) {
                            flag = true;  // 검은돌이 이김
                            startX = i;
                            startY = j;
                            winColor = 1;
                            break outer;
                        }
                    }
                } else if (data[i][j] == 2) {
                    for (int d = 0; d < 4; d++) {
                        if (BFS(i, j, 2, d)) {
                            if (BFS(i, j, 2, d)) {
                                flag = true;
                                startX = i;
                                startY = j;
                                winColor = 2;
                                break outer;
                            }
                        }
                    }
                }
            }
        }

        if (flag) {
            System.out.println(winColor);
            System.out.println(startX + " " + startY);
        } else {
            System.out.println(0);
        }

    }

    public static boolean BFS(int x, int y, int color, int d) { // 시작 좌표 x,y , 색깔, 방향 d
        int cnt = 1;
        int nx = x, ny = y;
        for (int i = 0; i < 4; i++) {
            nx += dx[d];
            ny += dy[d];
            if (isInner(nx, ny) && data[nx][ny] == color) {
                cnt += 1;
            } else {
                break;
            }
        }
        if(cnt != 5) return false;  // 5개 확인했는데 아니면 일단 그냥 아님.
        // 시작점 끝점 예외처리
        nx += dx[d]; ny += dy[d];
        // 끝점 예외처리
        if (isInner(nx, ny) && data[nx][ny] == color) {
            return false;
        }
        x -= dx[d]; y -= dy[d];
        // 시작점 예외처리
        if (isInner(x, y) && data[x][y] == color) {
            return false;
        }
        return true;
    }

    public static boolean isInner(int i, int j) {
        if (i < 1 || i > 19 || j < 1 || j > 19) {
            return false;
        }
        return true;
    }

    public static boolean checkRight(int x, int y, int color) {
        int cnt = 0;
        for (int i = 0; i < 5; i++) {
            if (isInner(x, y + i) && data[x][y + i] == color) {
                cnt += 1;
            }
        }
        if (cnt != 5) return false;
        if (cnt == 5) {
            // 여기서 이제 유효성 검사 진행
            if (isInner(x, y - 1) && (data[x][y - 1] == color)) {
                return false;
            }
            if (isInner(x, y + 5) && data[x][y + 5] == color) {
                return false;
            }
        }
        return true;
    }

    public static boolean checkDown(int x, int y, int color) {
        int cnt = 0;
        for (int i = 0; i < 5; i++) {
            if (isInner(x + i, y) && data[x + i][y] == color) {
                cnt += 1;
            }
        }
        if (cnt != 5) return false;
        if (cnt == 5) { // 시작점 -1, 끝점 + 1 기준으로 검사해야함
            if (isInner(x - 1, y) && data[x - 1][y] == color) {
                return false;
            }
            if (isInner(x + 5, y) && data[x + 5][y] == color) {
                return false;
            }
        }
        return true;
    }

    public static boolean checkDiagonalDown(int x, int y, int color) {
        int cnt = 0;
        for (int i = 0; i < 5; i++) {
            if (isInner(x + i, y + i) && data[x + i][y + i] == color) {
                cnt += 1;
            }
        }
        if (cnt != 5) return false;
        if (cnt == 5) { // 시작점 -1, 끝점 + 1 기준으로 검사해야함
            if (isInner(x - 1, y - 1) && data[x - 1][y - 1] == color) {
                return false;
            }
            if (isInner(x + 5, y + 5) && data[x + 5][y + 5] == color) {
                return false;
            }
        }
        return true;
    }

    public static boolean checkDiagonalUp(int x, int y, int color) {
        int cnt = 0;
        for (int i = 0; i < 5; i++) {
            if (isInner(x - i, y + i) && data[x - i][y + i] == color) {
                cnt += 1;
            }
        }
        if (cnt != 5) return false;
        if (cnt == 5) { // 시작점 -1, 끝점 + 1 기준으로 검사해야함
            if (isInner(x + 1, y - 1) && data[x + 1][y - 1] == color) {
                return false;
            }
            if (isInner(x - 5, y + 5) && data[x - 5][y + 5] == color) {
                return false;
            }
        }
        return true;
    }

}
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

    // 모든 입력 처리 후 게임 맵의 상태가 어떤지 확인.
    static int T, H, W; // ! 테케 수, 높이, 너비

    /**
     * ! 문자 의미
     * ! .	평지(전차가 들어갈 수 있다.)
     * ! *	벽돌로 만들어진 벽
     * ! #	강철로 만들어진 벽
     * ! -	물(전차는 들어갈 수 없다.)
     * ! ^	위쪽을 바라보는 전차(아래는 평지이다.)
     * ! v	아래쪽을 바라보는 전차(아래는 평지이다.)
     * ! <	왼쪽을 바라보는 전차(아래는 평지이다.)
     * ! >	오른쪽을 바라보는 전차(아래는 평지이다.)
     */

    /**
     * * 조건1. 좌표 내부인 경우만 움직일 수 있음
     * * 조건2. 포탄 발사 시 벽돌 벽 or 강철 벽 충돌하거나 게임 맵 밖으로 나갈 때까지 직진
     * * 조건3. 포탄이 벽돌 벽에 부딪히면 벽은 파괴, 해당 칸은 평지
     * * 조건4. 포탄이 강철 벽에 부딪히면 아무일도 X, 포탄이 맵 밖으로 나가더라도 아무 일도 X
     */
    static char up = 'U', down = 'D', left = 'L', right = 'R', shoot = 'S';
    static char brick_wall = '*', steel_wall = '#';  // 벽돌 벽, 강철 벽
    static char direction, pos = 'Q';  // 현재위치를 나타낼 pos
    static char[][] g;
    // ! 방향은 위(0) 오른쪽(1) 아래(2) 왼쪽(3) 순
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};
    static int x,y;  // 현재 좌표
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        T = Integer.parseInt(br.readLine()); // 테스트 케이스
        for (int t = 1; t <= T; t++) {
            st = new StringTokenizer(br.readLine());
            H = Integer.parseInt(st.nextToken()); // 높이
            W = Integer.parseInt(st.nextToken()); // 너비
            g = new char[H][W];
            for (int i = 0; i < H; i++) {
                String map = br.readLine();
                for (int j = 0; j < W; j++) {
                    g[i][j] = map.charAt(j);
                    if (g[i][j] == '>' || g[i][j] == 'v' || g[i][j] == '<' || g[i][j] == '^') {
                        x = i;
                        y = j;  // 현재 위치 갱신
                        // 방향 갱신
                        if(g[i][j] == '>') direction = right;
                        else if(g[i][j] == '<') direction = left;
                        else if(g[i][j] == '^') direction = up;
                        else if(g[i][j] == 'v') direction = down;
                        g[i][j] = pos;  // 좌표에 현재 위치 표시
                    }
                }
            }
            int cnt = Integer.parseInt(br.readLine());
            String command = br.readLine();  // 명렁어
            solve(command);
            switchChar();
            System.out.print("#" + t + " ");
            printResult();
        }
    }

    public static void switchChar() {
        switch(direction) {
            case 'U':
                g[x][y] = '^';
                break;
            case 'L':
                g[x][y] = '<';
                break;
            case 'R':
                g[x][y] = '>';
                break;
            case 'D':
                g[x][y] = 'v';
                break;
        }
    }

    public static boolean isInner(int x, int y) {
        if (x >= 0 && x < H && y >= 0 && y < W) {
            return true;
        }
        return false;
    }

    public static void solve(String commands) {
        for (char command : commands.toCharArray()) {
//            System.out.println("이번 명령어 : " + command + " 현재 전차 방향 : " + direction);
            if (command == up) {  // ! 방향을 up으로 바꾸고, 한칸 이동
                direction = up;  // 1. 방향 변경
                move(0);
            } else if (command == right) {
                direction = right;
                move(1);
            } else if (command == down) {
                direction = down;
                move(2);
            } else if (command == left) {
                direction = left;
                move(3);
            } else if (command == shoot) {
                // ! 현재 방향으로 포 발사
                fire();  // 현재 방향으로 포 발사
            }
//            System.out.println("명령어 후 현재 위치 : " + "(" + x + ", " + y + ")");
//            printMap();
        }
    }

    // ! now_x,now_y -> nx,ny로 이동
    public static void move(int d) {
        int nx = x + dx[d];
        int ny = y + dy[d];
        if (isInner(nx, ny) && g[nx][ny] == '.') { // ! 좌표 내부이면서 이동할 좌표 평지라면
            g[x][y] = '.';  // 현재 좌표 평지화
            x = nx; y = ny;  // 위치 갱신
            g[nx][ny] = pos;  // 위치 갱신
        }
    }

    public static void fire() {
        if (direction == up) {  // 위로 발포
            boom(x,y,0);
        } else if (direction == right) {
            boom(x,y,1);
        } else if (direction == down) {
            boom(x,y,2);
        } else if (direction == left) {
            boom(x,y,3);
        }
    }

    public static void boom(int p_x, int p_y, int d) {
        // ! p_x, p_y는 포탄 위치
        int nx = p_x;
        int ny = p_y;
        while (true) {
            nx = nx + dx[d];
            ny = ny + dy[d];
            if (isInner(nx, ny)) {  // 포탄이 좌표 내부인 경우만 이동
                if (g[nx][ny] == brick_wall) {  // 벽돌벽 만나면 파괴 후 평탄화
                    g[nx][ny] = '.';  // 평 지
                    break;
                } else if (g[nx][ny] == steel_wall) {  // 강철 만나면 끝내기
                    break;
                }
            } else {   // 맵 벗어나면 탈출
                break;
            }
        }
    }
    public static void printResult() {
        for (int i = 0; i < H; i++) {
            for (int j = 0; j < W; j++) {
                System.out.print(g[i][j]);
            }
            System.out.println();
        }
    }
}
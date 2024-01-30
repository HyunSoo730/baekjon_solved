import java.io.*;
import java.util.StringTokenizer;

public class Solution {

    static int[][] data = new int[100][100];
    static int n;
    static int dx[] = {0, 0, -1};
    static int dy[] = {-1, 1, 0};
    static int MAX_SIZE = 100;
    static int startPoint;
    static int a,b;  // 탐색 시작 위치
    static boolean flag;
    static boolean[][] visited;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        for (int t = 1; t <= 10; t++) {
            n = Integer.parseInt(br.readLine());
            for (int i = 0; i < 100; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < 100; j++) {
                    data[i][j] = Integer.parseInt(st.nextToken());
                }
            }
            // 계산 과정
            // 일단 도착지점의 좌표 찾기
            int v = 0;
            for (int i = 0; i < 100; i++) {
                if (data[MAX_SIZE - 1][i] == 2) {
                    v = i;
                    a = MAX_SIZE-1;
                    b = i;
                    break;
                }
            }
            visited = new boolean[100][100];
            flag = false;
            // 중복 체크 , flag는 초기화 후에 계속 진행.
            DFS(a,b);
            System.out.println("#" + t + " " + startPoint);
        }
    }


    public static void DFS(int x, int y) {
        if(flag) return;
        if (x == 0) {
            flag = true;
            startPoint = y;
        } else {
            for (int i = 0; i < 3; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if(isInner(nx, ny) && !visited[nx][ny] && data[nx][ny] == 1){ // 좌표 내부이면서, 좌표가
                    visited[nx][ny] = true; // 방문 처리 후
                    DFS(nx,ny);
                    visited[nx][ny] = false;
                }
            }
        }
    }

    public static boolean isInner(int x, int y) {
        if (x < 0 || x > MAX_SIZE - 1 || y < 0 || y > MAX_SIZE - 1) {
            return false;
        }
        return true;
    }
}
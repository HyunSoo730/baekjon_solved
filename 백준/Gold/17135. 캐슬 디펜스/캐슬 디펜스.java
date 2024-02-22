import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int n, m, D, cnt, maxCnt = Integer.MIN_VALUE, minDis;  // 행 열, 궁수의 공격 거리 d
    static int[][] g, copy;
    static List<Point> enemy = new ArrayList<>();
    static int[] pos;
    static boolean[] visited;
    private static class Point{
        int x, y;

        Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    // ! 0은 빈칸 1은 적
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        D = Integer.parseInt(st.nextToken());  // 최소 거리
        g = new int[n][m];
        copy = new int[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                g[i][j] = Integer.parseInt(st.nextToken());
                if (g[i][j] == 1) {
                    enemy.add(new Point(i, j));
                }
            }
        }
        pos = new int[3];  // 궁수의 y좌표

        // ! 궁수 최대 3명 배치
        DFS(0, 0);
        System.out.println(maxCnt);
    }

    public static void copy() {
        for (int i = 0; i < n; i++) {
            copy[i] = Arrays.copyOf(g[i], g[i].length);
        }
    }

    public static void DFS(int start, int L) {
        if (L == 3) {
            // 궁수의 위치 선택 완료 -> 거리 계산 진행
            visited = new boolean[enemy.size()];
            cnt = 0;
            killEnemy();
            maxCnt = Math.max(maxCnt, cnt);
        } else {
            for (int i = start; i < m; i++) {
                pos[L] = i;  // L 번째 궁수의 y좌표 i
                DFS(i + 1, L + 1);
            }
        }
    }

    public static void killEnemy() {
        int turn = 0;
        boolean[] check = new boolean[enemy.size()];
        while (turn < n) {   //총 n번 위로 올라갈 수 있음
            for (int i = 0; i < 3; i++) {
                Point now = new Point(n - turn, pos[i]);  // 현재 궁수의 좌표.
                minDis = Integer.MAX_VALUE;
                int left = Integer.MAX_VALUE;
                int index = -1;  //현재 궁수가 죽여야 하는 적
                for (int j = 0; j < enemy.size(); j++) {
                    if(check[j]) continue;  // 이미 죽인 적은 넘겨
                    Point en = enemy.get(j);  // 적 하나씩 꺼내기
                    if(now.x <= en.x) continue;  // 이미 현재 좌표를 넘어가면 확인하면 안돼
                    int dis = Math.abs(now.x - en.x) + Math.abs(now.y - en.y);
                    if(dis > D) continue;  // D보다 크면 넘겨
                    if (dis <= minDis) {
                        if (dis == minDis) {  // 같은 경우 왼쪽 적 죽여야함.
                            if (en.y < left) {
                                index = j;  // 현재 적을 기억
                                left = en.y;
                            }
                        } else {
                            minDis = dis;  // 최단거리 갱신했어야 했음.
                            index = j;
                            left = en.y;
                        }
                    }
                }
                if (index != -1) {
                    visited[index] = true;
                }
            }
            // 다 체크 후 확인
            for (int k = 0; k < enemy.size(); k++) {
                if(visited[k]) check[k] = true;
            }
            turn += 1;
        }
        for (int i = 0; i < enemy.size(); i++) {
            if(check[i]){
                cnt += 1;
            }
        }
    }
}
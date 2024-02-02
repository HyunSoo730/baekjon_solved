import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;


class Point{
    int x, y;

    Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}
public class Main {
    // 0 빈칸 1 집 2 피자집
    // 피자배달거리 : |x1-y2| + |y1-y2|
    // 피자집 중 m개만 선택.
    static int n,m;
    static int minDis = Integer.MAX_VALUE;
    static int[][] g;
    static List<Point> home, chicken;  // 집, 치킨집 저장
    static int[] res;  // 선택한 치킨집들 인덱스
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        g = new int[n+1][n+1];
        res = new int[m];  // 뽑은 피자집을 저장할 배열
        home = new ArrayList<>();
        chicken = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= n; j++) {
                g[i][j] = Integer.parseInt(st.nextToken());
                if(g[i][j] == 1) home.add(new Point(i, j));  // 집
                else if(g[i][j] == 2) chicken.add(new Point(i, j));  // 피자집
            }
        }
        // 세팅 끝.
        DFS(0, 0);
        System.out.println(minDis);
    }

    public static void DFS(int start, int L) {
        if (L == m) { // m개 선택. 종료 조건
            // 이제 선택된 m개에서의 최단거리 확인.
            int sum = calDis();
            if (sum < minDis) {
                minDis = sum;
            }
        } else {
            for (int i = start; i < chicken.size(); i++) {
                res[L] = i;
                DFS(i + 1, L + 1);
            }
        }
    }

    public static int calDis() {
        int sum = 0;
        for (int i = 0; i < home.size(); i++) {  // 집 기준으로 계산해야함.
            int dis = Integer.MAX_VALUE;
            for (int j = 0; j < res.length; j++) {
                dis = Math.min(dis, Math.abs(home.get(i).x - chicken.get(res[j]).x) + Math.abs(home.get(i).y - chicken.get(res[j]).y));
            }
            sum += dis;
        }
        return sum;
    }
}
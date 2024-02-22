import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.StringTokenizer;

public class Solution {

    // ! 비상 연락망과 연락을 시작하는 당번에 대한 정보가 주어질 때, 가장 나중에 연락을 받게 되는 사람 중 번호가 가장 큰 사람을 구하는 함수

    static int n, start;  // 입력받는 데이터 길이, 시작점
    static ArrayList<ArrayList<Integer>> g = new ArrayList<>();
    static boolean[] visited;
    static int res, maxNum;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        for (int t = 1; t <= 10; t++) {
            st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            start = Integer.parseInt(st.nextToken());
            g = new ArrayList<ArrayList<Integer>>();
            for (int i = 0; i <= 100; i++) {
                g.add(new ArrayList<Integer>());
            }

            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n / 2; i++) {
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                g.get(a).add(b); // a->b 가능
            }
            maxNum = Integer.MIN_VALUE;
            BFS(start);
            sb.append("#").append(t).append(" ").append(maxNum).append("\n");
        }
        System.out.println(sb);
    }

    public static void BFS(int start) {
        visited = new boolean[101];  // ! 들어오는 배열만 체크했으면 됐음. 2차원으로 해서 틀린 결과가 나옴.
        Deque<Integer> dq = new ArrayDeque<>();
        dq.offer(start);
        while (!dq.isEmpty()) {
            int size = dq.size();
//            System.out.print("<레벨 : " + cnt + ", " + "연결된 노드 : ");
            int cnt = 0;
            res = 0;  // 매 레벨마다 반복.
            for (int i = 0; i < size; i++) {  // * 레벨 단위로 진행
                int now = dq.poll();
                for (int node : g.get(now)) {
//                    System.out.print(node + " ");
                    if (!visited[node]) { // ! now -> node 아직 안갔다면 방문처리 후 진행
                        visited[node] = true;
                        res = Math.max(res, node);
                        dq.offer(node);
                        cnt += 1;
                    }
                }
            }
            if(cnt == 0) break;
            maxNum = res;  // 레벨이 끝날 때마다 maxNum 갱신
        }
    }
}
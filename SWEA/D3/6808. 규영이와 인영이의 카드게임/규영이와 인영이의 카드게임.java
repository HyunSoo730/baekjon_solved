import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

    // ! 1~18 카드. 9장씩 나눔. 9라운드 게임
    // ! 각 라운드 별로 한 장씩 서로 비교 후 점수 계산.

    static int T;
    static int[] dataA, dataB, selectedCard;
    static boolean[] visited;
    static int win, lose;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        T = Integer.parseInt(br.readLine());
        for (int t = 1; t <= T; t++) {
            dataA = new int[9];
            dataB = new int[9];
            st = new StringTokenizer(br.readLine());
            boolean[] cardCheck = new boolean[19];
            for (int i = 0; i < 9; i++) {
                dataA[i] = Integer.parseInt(st.nextToken());
                cardCheck[dataA[i]] = true;
            }
            int idx = 0;
            for (int i = 1; i <= 18; i++) {
                if (!cardCheck[i]) {
                    dataB[idx++] = i;
                }
            }
            // 규영, 인영 카드 모두 채움
            win = lose = 0;
            visited = new boolean[9];
            selectedCard = new int[9];
            DFS(0);
//            System.out.println("wins : " + win + " lose : " + lose);
            sb.append("#" + t).append(" ").append(win).append(" ").append(lose).append("\n");
        }
        System.out.println(sb);
    }

    public static void DFS(int L) {
        if (L == 9) {  // 9개 선택 종료조건.
            // 이제 선택된 카드와 비교 -> 규영이가 이기는 경우의 수와 지는 경우의 수
            int sumA=0, sumB = 0;   // 인영, 규영
            for (int i = 0; i < 9; i++) {
                if (selectedCard[i] > dataB[i]) {
                    sumA += selectedCard[i] + dataB[i];
                } else if(selectedCard[i] < dataB[i]) {
                    sumB += selectedCard[i] + dataB[i];
                }
            }
            if(sumA > sumB) win += 1;
            else if(sumA < sumB) lose += 1;

        } else {
            for (int i = 0; i < 9; i++) {
                if (!visited[i]) {
                    visited[i] = true;
                    selectedCard[L] = dataA[i];  // 인영 선택
                    DFS(L + 1);
                    visited[i] = false;
                }
            }
        }
    }

}
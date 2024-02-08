import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Data implements Comparable<Data>{
    int sco, cal;

    Data(int sco, int cal) {
        this.sco =sco;
        this.cal = cal;
    }

    @Override
    public int compareTo(Data o) {
        return o.sco - this.sco;  // 점수 내림차순
    }
}
public class Solution {

    /**
     * ! 정해진 칼로리 넘지 않도록.
     * ! 재료 (점수, 칼로리)
     * ! 재료는 한 번만 사용 가능.
     */

    static int T, n, limit;   // 테스트 케이스, 재료 수, 제한 칼로리
    static Data[] data;
    static int res;
    static int totalScore;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        T = Integer.parseInt(br.readLine());
        for (int t = 1; t <= T; t++) {
            st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            limit = Integer.parseInt(st.nextToken());
            data = new Data[n];
            totalScore = 0;
            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                int sco = Integer.parseInt(st.nextToken());
                int cal = Integer.parseInt(st.nextToken());
                data[i] = new Data(sco, cal);
                totalScore += sco;
            }
            res = Integer.MIN_VALUE;  // 높은 점수 저장 위해 초기화
            DFS(0, 0, 0);
            System.out.println("#" + t + " " + res);
        }
    }

    public static void DFS(int L, int scoreSum, int calorieSum) {
        if(calorieSum > limit)  // 가지 치기
            return;
        if (L == n) {  // 모든 인덱스 확인. 끝
            if (scoreSum > res) {
                res = scoreSum;
            }
        } else {
            DFS(L + 1, scoreSum + data[L].sco, calorieSum + data[L].cal);  // 현재 추가
            DFS(L + 1, scoreSum, calorieSum);
        }
    }

}
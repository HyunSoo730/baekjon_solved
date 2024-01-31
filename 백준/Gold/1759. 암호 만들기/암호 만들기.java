import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {


    static int n, m;  // n개 최종 암호 길이, m개 원소 -> m개중 n개 선택
    static Character[] data;
    static Character[] res;
    static Character[] check = {'a', 'e', 'i', 'o', 'u'};
    static int count = 0;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        data = new Character[m];
        res = new Character[n];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            data[i] = st.nextToken().charAt(0);
        }
        Arrays.sort(data);
        DFS(0, 0); // 0번째 인덱스부터 선택할 것이고, 몇개 뽑았는지 체크
        System.out.println(sb);
    }

    public static void DFS(int start, int L) {
        if (L == n) { // 다 뽑음 종료조건.
            // 모음 개수, 자음 개수 확인
            int cntA = 0; // 모음 개수
            int cntB = 0; // 자음 개수
            Set<Character> set = new HashSet<>(Arrays.asList(check));
            for (int i = 0; i < n; i++) {
                if (set.contains(res[i])) {
                    cntA += 1;
                } else {
                    cntB += 1;
                }
            }
            if (cntA >= 1 && cntB >= 2) {
                for (int i = 0; i < n; i++) {
                    sb.append(res[i]);
                }
                sb.append("\n");
            }
        } else {  // 아직 다 뽑지 못함 -> 더 뽑아야함.
            for (int i = start; i < m; i++) {
                res[L] = data[i];   // 백트랙킹 시 알아서 해당 자리에 삽입됨.
                DFS(i + 1, L + 1);
            }
        }
    }
}
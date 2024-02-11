import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static int n;
    static int[][] g;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        g = new int[n][n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                g[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // i -> j까지 갈 수 있는가?
        // ! i->k로 가고, k에서 j로 갈 수 있는가?
        // ! 위에 두 질문은 동일하다.
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    // 단순히 경로가 존재하는지만 체크
                    if (g[i][k] == 1 && g[k][j] == 1) {
                        g[i][j] = 1;
                    }
                }
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(g[i][j] + " ");
            }
            System.out.println();
        }
    }
}
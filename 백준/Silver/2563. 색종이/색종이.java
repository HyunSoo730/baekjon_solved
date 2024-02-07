import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;



public class Main {

    static int n;
    static int[][] g;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        g = new int[101][101];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int y = Integer.parseInt(st.nextToken());
            int x = Integer.parseInt(st.nextToken());
            for (int nx = x; nx < x + 10; nx++) {
                for (int ny = y; ny < y + 10; ny++) {
                    g[nx][ny] = 1;
                }
            }
        }

        int cnt = 0;
        for (int i = 1; i < 101; i++) {
            for (int j = 1; j < 101; j++) {
                if (g[i][j] == 1) {
                    cnt +=1;
                }
            }
        }
        System.out.println(cnt);
    }

}
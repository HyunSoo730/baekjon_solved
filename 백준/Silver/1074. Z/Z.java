import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static int n,r,c, cnt;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        n = (int) (Math.pow(2, n) * Math.pow(2, n));

//        System.out.println(n + " " + r + " " + c);
        DFS(n, 0, 0);
        System.out.println(cnt);
    }

    public static void DFS(int size, int row, int col) {
        if (size == 1) {
            return;
        } else {
            size /= 2;
            if (r < row + size && c < col + size) {  // 1사분면
                cnt += (size*size) * 0;
                DFS(size, row, col);  // 1사분면에 있으므로 그대로 진행
            } else if (r < row + size && c >= col + size) { // 2사분면
                cnt += (size * size) * 1;
                DFS(size, row, col + size);
            } else if (r >= row + size && c < col + size) { // 3사분면
                cnt += (size * size) * 2;
                DFS(size, row + size, col);
            } else if (r >= row + size && c >= col + size) {
                cnt += (size * size) * 3;
                DFS(size, row + size, col + size);
            }
        }
    }
}
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    // ! 3,5봉지로 정확하게 n 얻기 + 최대한 적은 봉지 사용
    static int n;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        int cnt = 0;
        boolean flag = true;
        while (n > 0) {
            if (n % 5 == 0) {
                cnt += n / 5;
                n /= 5;
                break;
            } else {
                cnt += 1;
                n -= 3;
            }
        }
        if(n < 0) System.out.println(-1);
        else System.out.println(cnt);
    }

}
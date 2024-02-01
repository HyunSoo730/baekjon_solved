import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static int n;
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        DFS(1, 2);
        DFS(1, 3);
        DFS(1, 5);
        DFS(1, 7);
        System.out.println(sb);
    }

    public static void DFS(int L, int num) { // 자릿수, 현재 숫자
        if (L == n) { // n번째 자리 수 도착하면 이제 해당 수가 '신기한 소수'임을 확인가능
            System.out.println(num);
        } else {
            for (int i = 1; i <= 9; i+=2) {  // 애초에 짝수도 소수가 될 수 없음.
                int nextNum = num*10 + i;
                // 해당 수 소수 판별
                if (isPrimeNum(nextNum)) {
                    DFS(L + 1, nextNum);  // 소수인 경우만 다음 단계로 이동.
                }
            }
        }
    }

    public static boolean isPrimeNum(int num) {
        for (int i = 2; i <= (int) Math.sqrt(num); i++) {
            if(num % i == 0)
                return false;
        }
        return true;
    }
}
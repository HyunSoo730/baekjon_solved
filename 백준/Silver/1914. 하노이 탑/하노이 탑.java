import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.StringTokenizer;

public class Main {

    static int n;


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        n = Integer.parseInt(br.readLine());
        BigInteger count = new BigInteger("2");
        System.out.println(count.pow(n).subtract(new BigInteger("1")));
        if (n <= 20) {
            DFS(n, 1, 2, 3);
        }
    }

    //n은 남은 원판, start은 옮기는 위치, end는 도착 위치 temp는 중간 거쳐가는 위치
    public static void DFS(int n, int start, int temp, int end) {
        if (n == 1) {  // 종료조건
            System.out.println(start + " " + end);  // 시작점, 끝점 출력
        } else {
            DFS(n - 1, start, end, temp);
            System.out.println(start + " " + end);
            DFS(n - 1, temp, start, end);
        }
    }
}
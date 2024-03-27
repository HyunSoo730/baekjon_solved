import java.awt.*;
import java.io.*;
import java.util.*;
import java.util.List;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int[][] g;
    private static class Point{
        int x, y;

        Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    static List<Point> blank = new ArrayList<>();
    public static void main(String[] args) throws IOException {

        g = new int[9][9];
        for (int i = 0; i < 9; i++) {
            String data = br.readLine();
            for (int j = 0; j < 9; j++) {
                g[i][j] = data.charAt(j) - '0';
            }
        }

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (g[i][j] == 0) {
                    blank.add(new Point(i, j));
                }
            }
        }

        DFS(0);

    }

    public static void DFS(int L){
        if (L == blank.size()) { // ! 모두 확인
            for (int i = 0; i < 9; i++) {
                for (int j = 0; j < 9; j++) {
                    System.out.print(g[i][j]);
                }
                System.out.println();
            }
            System.exit(0);
        } else {
            Point now = blank.get(L);
            int x = now.x;
            int y = now.y;
            for (int i = 1; i <= 9; i++) {
                // ! x,y 자리에 어울리는지 판단
                if(check_box(x,y,i) && check_row(x,y,i) && check_col(x,y,i)){
                    g[x][y] = i; // ! 해당 값 가능
                    DFS(L+1); // ! 다음으로 가서 다시 확인
                    g[x][y] = 0; // ! 백트랙킹 시 원상 복구
                }
            }
        }
    }

    public static boolean check_row(int x, int y, int val) {
        // ! 행 체크 -> 행 고정 열 변수
        for (int i = 0; i < 9; i++) {
            if(g[x][i] == val) return false;
        }
        return true;
    }

    public static boolean check_col(int x, int y, int val) {
        // ! 열 체크 -> 열 고정 행 변수
        for (int i = 0; i < 9; i++) {
            if(g[i][y] == val) return false;
        }
        return true;
    }

    public static  boolean check_box(int x, int y, int val){
        // ! 3x3 확인
        int dx = (x/3) * 3;
        int dy = (y/3) * 3;
        for (int i = dx; i < dx + 3; i++) {
            for (int j = dy; j < dy + 3; j++) {
                if(g[i][j] == val) return false;
            }
        }
        return true;
    }

}
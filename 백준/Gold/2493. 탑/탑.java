import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

class Data {
    int idx;
    int val;

    Data(int idx, int val) {
        this.idx = idx;
        this.val = val;
    }
}
public class Main {

    static int n;
    static int[] data, res;
    static Stack<Data> stack = new Stack<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        data = new int[n];
        for (int i = 0; i < n; i++) {
            data[i] = Integer.parseInt(st.nextToken());
        }
        res = new int[n];

        for (int i = 0; i < n; i++) {
            if (stack.isEmpty()) {
                res[i] = 0;
                stack.push(new Data(i, data[i]));
            } else if (stack.peek().val > data[i]) {
                res[i] = stack.peek().idx+1;
                stack.push(new Data(i, data[i]));
            } else if (stack.peek().val < data[i]) {
                while (!stack.isEmpty()) {
                    if (stack.peek().val < data[i]) {
                        stack.pop();
                    } else {
                        res[i] = stack.peek().idx+1;
                        stack.push(new Data(i, data[i]));
                        break;
                    }
                }
                if (stack.isEmpty()) {
                    res[i] = 0;
                    stack.push(new Data(i, data[i]));
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            sb.append(res[i]).append(" ");
        }
        System.out.println(sb);
    }
}
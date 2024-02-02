import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Solution {

    static Stack<Character> stack = new Stack<>();
    static int T, n;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        for (int t = 1; t <= 10; t++) {
            n = Integer.parseInt(br.readLine());
            String data = br.readLine();
            if (checkBrackets(data)) {
                System.out.println("#" + t + " " + 1);
            } else {
                System.out.println("#" + t + " " + 0);
            }
        }
    }

    public static boolean checkBrackets(String data) {
        for (char c : data.toCharArray()) {
            if (c == '(' || c == '[' || c == '{' || c == '<') {
                stack.push(c);
            }
            if (c == ')') {
                if (stack.pop() != '(') {
                    return false;
                }
            } else if (c == ']') {
                if (stack.pop() != '[') {
                    return false;
                }
            } else if (c == '}') {
                if (stack.pop() != '{') {
                    return false;
                }
            } else if (c == '>') {
                if (stack.pop() != '<') {
                    return false;
                }
            }
        }
        return true;
    }
}
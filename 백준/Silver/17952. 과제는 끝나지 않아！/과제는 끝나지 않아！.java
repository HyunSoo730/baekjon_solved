import java.io.*;
import java.util.*;
public class Main {
	
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	
	private static class Data{
		int score, time;
		Data(int score, int time){
			this.score = score;
			this.time = time;
		}
	}
	
	static int n;
	static Stack<Data> stack = new Stack<>();
	static long res;
	
	public static void main(String[] args) throws IOException {

		n = Integer.parseInt(br.readLine());
		for(int i=1;i<=n;i++) {
			st = new StringTokenizer(br.readLine());
			int oper = Integer.parseInt(st.nextToken());
			if(oper == 0) {  // 기존 업무 수행
				if(!stack.isEmpty()) {
					Data data = stack.pop();
					data.time -= 1;
					if(data.time == 0) {
						res += data.score;
					}else {
						stack.push(data);
					}
				}
			}else {  // 새로운 업무 수행
				int score = Integer.parseInt(st.nextToken());
				int time = Integer.parseInt(st.nextToken());
				Data data = new Data(score, time);
				data.time -= 1;  // ㅎ해당 업무 수행 후 삽입
				if(data.time == 0) {  // 바로 끝냄
					res += data.score;
				}else {
					stack.push(data);
				}
			}
		}
		
		System.out.println(res);
	}

}
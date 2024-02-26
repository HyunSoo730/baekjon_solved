import java.io.*;
import java.util.*;

public class Main {
	
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	
	
	static int n, m;
	static List<List<Integer>> g = new ArrayList<>();
	static int res;
	
	public static void main(String[] args) throws IOException {
		
		n = Integer.parseInt(br.readLine());
		m = Integer.parseInt(br.readLine());
		
		for(int i=0;i<=n;i++) {
			g.add(new ArrayList<Integer>());
		}
		
		for(int i=0;i<m;i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			g.get(a).add(b);
			g.get(b).add(a);
		}
		
		BFS(1);
		System.out.println(res);
	}
	
	public static void BFS(int v) {
		Deque<Integer> dq = new ArrayDeque<>();
		boolean[] visited = new boolean[n+1];
		dq.offer(v);
		visited[v] = true;
		
		while(!dq.isEmpty()) {
			Integer now = dq.poll();
			
			for(Integer node : g.get(now)) {
				if(!visited[node]) {
					visited[node] = true;
					dq.offer(node);
					res += 1;
				}
			}
		}
	}

}
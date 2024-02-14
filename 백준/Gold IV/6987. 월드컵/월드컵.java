import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    private static class Team{
        int win;
        int draw;
        int lose;

        Team(int win, int draw, int lose) {
            this.win = win;
            this.draw = draw;
            this.lose = lose;
        }
    }
    static boolean flag;
    static Team[] teams;
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        teams = new Team[6];
        for (int i = 0; i < 4; i++) {
            st = new StringTokenizer(br.readLine());
            int total = 0;
            for (int t = 0; t < 6; t++) {
                teams[t] = new Team(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
                total += teams[t].win + teams[t].draw + teams[t].lose;
            }
            flag = false;
            if (total == 30) {
                DFS(0, 1);
            }
            sb.append(flag ? 1 : 0).append(" ");

        }
        System.out.println(sb);

    }

    public static void DFS(int team1, int team2) {
        if(flag) return;
        if (team1 == 5) {
            flag = true;
            return;
        }
        if(team2 == 6) { // 한 팀의 모든 경기를 확인했으므로 다음 팀
            DFS(team1 + 1, team1 + 2);
        }

        // team1 승리, team2 패배
        if (teams[team1].win > 0 && teams[team2].lose > 0) {
            teams[team1].win--;
            teams[team2].lose--;
            DFS(team1, team2 + 1);
            teams[team1].win++;
            teams[team2].lose++;
        }

        // 무승부
        if (teams[team1].draw > 0 && teams[team2].draw > 0) {
            teams[team1].draw--;
            teams[team2].draw--;
            DFS(team1, team2 + 1);
            teams[team1].draw++;
            teams[team2].draw++;
        }

        // team2 승리, team1 패배
        if (teams[team1].lose > 0 && teams[team2].win > 0) {
            teams[team1].lose--;
            teams[team2].win--;
            DFS(team1, team2 + 1);
            teams[team1].lose++;
            teams[team2].win++;
        }

    }
}
package cotestudy.완전탐색;
import java.io.*;
import java.util.*;
public class no19532 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken()), b = Integer.parseInt(st.nextToken()), c = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken()), e = Integer.parseInt(st.nextToken()), f = Integer.parseInt(st.nextToken());
        int x = 0;
        int y = 0;
        Outter:for (int i = -999; i < 1000; i++) {
            for (int j = -999; j < 1000; j++) {
                if (a * i + b * j == c && d * i + e * j == f) {
                    x = i;
                    y = j;
                    break Outter;
                }
            }
        }
        bw.write(x + " " + y);
        bw.flush();
        bw.close();
    }
}

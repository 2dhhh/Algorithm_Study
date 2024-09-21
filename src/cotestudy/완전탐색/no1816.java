package cotestudy.완전탐색;
import java.io.*;
import java.util.*;
public class no1816 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            long s = Long.parseLong(br.readLine());
            for (int j = 2; j < 1000001; j++) {
                if (s % j == 0) {
                    bw.write("NO\n");
                    break;
                }
                if (j == 1000000) {
                    bw.write("YES\n");
                }
            }

        }
        bw.flush();
        bw.close();
    }
}

package cotestudy.완전탐색;
import java.io.*;
import java.util.*;
public class no14697 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());
        String ans = "";

        Outter:for (int i = 0; i <= 300; i++) {
            for (int j = 0; j <= 150; j++) {
                for (int k = 0; k <= 100; k++) {
                    if (a * i + b * j + c * k == n) {
                        ans = "1";
                        break Outter;
                    }
                }
            }
            ans = "0";
        }
        bw.write(ans);
        bw.flush();
        bw.close();
    }
}

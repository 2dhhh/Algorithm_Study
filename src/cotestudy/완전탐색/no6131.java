package cotestudy.완전탐색;
import java.io.*;
public class no6131 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        int cnt = 0;

        for (int i = 1; i < 501; i++) {
            for (int j = 1; j <= i; j++) {
                if (i * i == j * j + n) {
                    cnt ++;
                }
            }
        }
        bw.write(cnt + "");
        bw.flush();
        bw.close();
    }
}

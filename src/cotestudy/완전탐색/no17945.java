package cotestudy.완전탐색;
import java.io.*;
import java.util.*;
public class no17945 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

        for (int i = -1000; i < 1001; i++) {
            if (i * i + 2 * a * i + b == 0) {
                bw.write(i + " ");
            }
        }
        bw.flush();
        bw.close();
    }
}

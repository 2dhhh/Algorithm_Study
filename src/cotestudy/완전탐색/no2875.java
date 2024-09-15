package cotestudy.완전탐색;
import java.io.*;
import java.util.*;
public class no2875 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int A = 0;
        int B = 0;
        int maxValue = 0;


        for (int i = 0; i <= K; i++) {
            A = N -i;
            B = M-K+i;
            int tmp = Math.min(A/2, B);
            if (tmp > maxValue) {
                maxValue = tmp;
            }
        }
        bw.write(maxValue + "");
        bw.flush();
        bw.close();
    }
}

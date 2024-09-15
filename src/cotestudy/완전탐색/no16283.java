package cotestudy.완전탐색;
import java.io.*;
import java.util.*;
public class no16283 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());
        int w = Integer.parseInt(st.nextToken());
        int sheep = 0;
        int goat = 0;
        int cnt = 0;

        for (int i = 1; i < n; i++) {
            if ((a - b) * i + b * n == w) {
                sheep = i;
                goat = n - sheep;
                cnt++;
            }
        }
        if(cnt == 1){
            bw.write(sheep + " " + goat);
        }
        else
            bw.write("-1");
        bw.flush();
        bw.close();
    }
}

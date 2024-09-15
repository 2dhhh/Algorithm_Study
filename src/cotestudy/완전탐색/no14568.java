package cotestudy.완전탐색;
import java.io.*;
public class no14568 {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());

        int A = 0;
        int B = 0;
        int C = 0;
        int ans = 0;

        for (int i = 1; i < N-2; i++) {
            A = i;
            for(int j = 1; j < N-2; j++) {
                B = j;
                C = N - i - j;
                if(A %2 == 0 && C >= B+2){
                    ans++;
                }
            }
        }
        bw.write(ans + "");
        bw.flush();
        bw.close();

    }

}

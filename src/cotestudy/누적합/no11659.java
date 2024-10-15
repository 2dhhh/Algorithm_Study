package cotestudy.누적합;
import java.io.*;
import java.util.*;
public class no11659 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] intArray = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            intArray[i] = Integer.parseInt(st.nextToken());
        }
        //누적합 배열 선언
        int[] prefix_sum = new int[n + 1];
        prefix_sum[0] = 0;
        for (int i = 1; i < n + 1; i++) {
            prefix_sum[i] = prefix_sum[i - 1] + intArray[i - 1];
        }

        for (int k = 0; k < m; k++) {
            st = new StringTokenizer(br.readLine());
            int i = Integer.parseInt(st.nextToken());
            int j = Integer.parseInt(st.nextToken());
            int ans = prefix_sum[j] - prefix_sum[i - 1];
            bw.write(ans +"\n");
        }
        bw.flush();
        bw.close();
    }
}

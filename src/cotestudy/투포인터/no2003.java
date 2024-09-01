package cotestudy.투포인터;
import java.io.*;
import java.util.StringTokenizer;

public class no2003 {

        // 투포인터 풀이
        public static void main(String[] args) throws IOException {

            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
            StringTokenizer st;
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());

            st = new StringTokenizer(br.readLine());
            int[] intArray = new int[n];
            for (int i = 0; i < n; i++) {
                intArray[i] = Integer.parseInt(st.nextToken());
            }
            br.close();

            int s = 0, e = 0, sum = 0, cnt = 0;
            while (true) {

                if (sum >= m) {
                    sum -= intArray[s++];
                }
                else if(e == n) break;

                else {
                    sum += intArray[e++];
                }
                if (sum == m) {
                    cnt++;
                }
            }
            bw.write(cnt + "");
            bw.flush();
            bw.close();
        }

        //완전탐색 풀이
    /*
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int[] intArray = new int[N];
        for (int i = 0; i < N; i++) {
            intArray[i] = Integer.parseInt(st.nextToken());
        }

        int sum = 0;
        int count = 0;

        for (int i = 0; i < N; i++) {
            sum += intArray[i];
            if (sum > M) {
                sum = 0;
                continue;
            }
            if (sum == M) {
                count++;
                sum = 0;
                continue;
            }

            if (i == N - 1) {
                break;
            }
            for (int j = i+1; j < N; j++) {
                sum += intArray[j];

                if (sum > M) {
                    sum = 0;
                    break;
                }
                if (sum == M) {
                    count++;
                    sum = 0;
                    break;
                }
            }
            sum = 0;
        }
        bw.write(count + "");
        bw.flush();
        bw.close();
    }
     */
}

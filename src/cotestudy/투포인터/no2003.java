package cotestudy.투포인터;
import java.io.*;
import java.util.StringTokenizer;

public class no2003 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int[] intArray = new int[n];
        for (int i = 0; i < n; i++) {
            intArray[i] = Integer.parseInt(st.nextToken());
        }
        //완전탐색 풀이
        int sum = 0;
        int count = 0;
        int s = 0, e = 0;
//        for (int i = 0; i < n; i++) {
//            sum = intArray[i];
//            if (sum == m) {
//                count++;
//                continue;
//            }
//            for (int j = i + 1; j < n; j++) {
//                if (i == n - 1) {
//                    break;
//                }
//                sum += intArray[j];
//                if (sum == m) {
//                    count++;
//                    break;
//                }
//            }
//        }
        //투포인터 풀이
        while (true) {
            if(sum >= m){
                sum -= intArray[s++];
            } else if (e == n) break;
              else {
                sum += intArray[e++];
            }
            if (sum == m) {
                count++;
            }
        }
        bw.write(count + "");
        bw.flush();
        bw.close();
    }
}

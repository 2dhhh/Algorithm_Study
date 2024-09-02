package cotestudy.투포인터;
import java.io.*;
import java.util.*;
public class no2467 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] intArray = new int[N];
        for (int i = 0; i < N; i++) {
            intArray[i] = Integer.parseInt(st.nextToken());
        }

        int s = 0; int e = N-1; int sum = 0; int ans = Integer.MAX_VALUE;
        int left = 0; int right = 0;

        while (s < e) {
            sum = intArray[s] + intArray[e];
            if(ans > Math.abs(sum)){
                ans = Math.abs(sum);
                left = s;
                right = e;
            }
            if(sum >= 0){
                e--;
            } else{
                s++;
            }
        }
        bw.write(intArray[left] + " " + intArray[right]);
        bw.flush();
        bw.close();
    }
}

package cotestudy.투포인터;
import java.io.*;
import java.util.*;
public class no3273 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        int[] intArray = new int[n];
        for (int i = 0; i < n; i++) {
            intArray[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(intArray);
        int x = Integer.parseInt(br.readLine());

        // 투 포인터 이용
        int s = 0, e = intArray.length - 1, count = 0;
        while(s < e){
            if(intArray[s] + intArray[e] == x){
                s++;
                e--;
                count++;
            } else if (intArray[s] + intArray[e] > x) {
                e--;
            } else s++;
        }
        bw.write(count + "");
        bw.flush();
        bw.close();

    }
}

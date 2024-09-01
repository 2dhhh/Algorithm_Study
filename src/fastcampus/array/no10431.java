package fastcampus.array;

import java.io.*;
import java.util.StringTokenizer;
public class no10431 {
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int t = Integer.parseInt(br.readLine());

        while(t > 0) {
            t--;
            StringTokenizer st = new StringTokenizer(br.readLine());
            String n = st.nextToken();

            int count = 0;
            int[] arr = new int[20];

            for (int i = 0; i < 20; i++) {
                arr[i] = Integer.parseInt(st.nextToken());
            }


            for (int i = 1; i < 20; i++) {
                for (int j = i - 1; j >= 0; j--) {
                    if (arr[i] < arr[j]) {
                        count ++;
                    }
                }
            }
            bw.write(n + " " + count + "\n");
        }
        bw.flush();
        bw.close();

    }
}

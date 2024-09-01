package fastcampus.brute_force;
import java.io.*;
import java.util.StringTokenizer;

public class no10250 {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        //테스트 케이스 입력
        int t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {
            //H, W, N 입력
            StringTokenizer st = new StringTokenizer(br.readLine());
            int h = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            int n = Integer.parseInt(st.nextToken());

            //층수
            int high = n%h;
            //호수
            int width = (n/h) + 1;

            if (high > 9) {
                System.out.printf("%d%02d", high, width);
            }
            else  {
                System.out.printf("%d%02d\n", high, width);
            }

        }



    }
}

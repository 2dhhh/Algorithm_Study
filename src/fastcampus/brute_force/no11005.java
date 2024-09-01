package fastcampus.brute_force;
import java.io.*;
import java.util.StringTokenizer;
public class no11005 {

    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

        int count = 0 ;
        int countNum = n;
        boolean check = true;

        //나머지 저장할 배열 선언 길이 36
        int[] intArr = new int[36];


        //총 몇번의 나눗셈을 진행해야 하는지 체크
        while (check) {
            if (countNum >= b) {
                count++;
                countNum /= b;
            }
            else {
                check = false;
                if (countNum >= 10) {
                    char c = (char)((countNum-10) +'A');
                    bw.write(String.valueOf(c));
                }
                else{
                    bw.write(String.valueOf(countNum));
                }

            }
        }
        int[] intArr2 = new int[count];

        //나머지 저장할 배열 선언 길이 36
        for (int i = 0; i < count; i++) {
            intArr2[i] = n % b;
            n /= b;
        }

        for (int i = count - 1; i >= 0; i--) {
            if (intArr2[i] >= 10) {
                char a = (char)((intArr2[i] - 10) + 'A');
                bw.write(a);
            }
            else {
                bw.write(String.valueOf(intArr2[i]));
            }
        }
        bw.flush();
        bw.close();
    }
}

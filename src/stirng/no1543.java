package stirng;
import java.io.*;

public class no1543 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        //몇 번 등장하는지 세는 변수
        int count = 0;
        int index = 0;

        String str1 = br.readLine();
        String str2 = br.readLine();

        while ((index = str1.indexOf(str2, index)) != -1) {
            count ++;
            index += str2.length();
        }
        bw.write(String.valueOf(count));
        bw.flush();
        bw.close();
    }
}

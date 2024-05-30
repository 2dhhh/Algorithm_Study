package stirng;


import java.util.Scanner;

public class no1543 {

        public static void main(String[] args) {

            Scanner sc = new Scanner(System.in);
            // 사용자로부터 입력
            String str1 = sc.nextLine();
            String str2 = sc.nextLine();

            int count = 0;
            int index = 0;

            while ((index = str1.indexOf(str2, index)) != -1) {
                count++;
                index += str2.length();
            }

            System.out.println(count);
        }
}

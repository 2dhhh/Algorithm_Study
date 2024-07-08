package array;

import java.util.Scanner;

public class no10431 {

    public static void main(String[] args) {

        // 입력
        Scanner sc = new Scanner(System.in);

        int t = sc.nextInt();

        while (t > 0) {
            t--;
            int tNum = sc.nextInt();

            int count = 0;
            int[] arr = new int[20];

            // 데이터 입력
            for (int i = 0; i < 20; i++) {
                arr[i] = sc.nextInt();
            }

            // 문제풀이 로직
            for (int i = 1; i < 20; i++) {
                for (int j = i - 1; j >= 0; j--) {
                    if(arr[j] > arr[i]){
                        count++;
                    }
                }
            }
            System.out.println(tNum + " " + count);
        }
    }
}

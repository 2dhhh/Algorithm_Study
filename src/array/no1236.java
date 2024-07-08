package array;

import java.util.Scanner;

public class no1236 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        //초기 설정
        int n,m;
        n = sc.nextInt();
        m = sc.nextInt();

        // 추가해야할 경비원수
        int count = 0;
        int max;

        //입력 값을 저장할 변수
        String[] bState = new String[n];

        //입력
        for(int i = 0; i < n; i++){
            bState[i] = sc.next();
        }

        //문제풀이 로직 -> 문자열 배열 하나씩 가져와서 문자로 전환 후 경비원 존재 여부 확인

        //1.문자열 배열 꺼내오기 -> 행을 통해 카운팅
        for(int i = 0; i < n; i++){
            String str = bState[i];
            if (str.contains("X")) continue;

            else count++;
        }
        max =count;
        count = 0;

        //2.열을 통한 경비원 카운팅
        for(int i = 0; i < m; i++){
            int counts = 0;
            for(int j = 0; j < n; j++){
                if(bState[j].charAt(i) == '.'){
                    counts++;
                }
            }
            if(counts == n)count++;
        }
        if(count > max){
            max = count;
        }

        System.out.println(max);



    }
}

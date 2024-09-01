package fastcampus.big_o;

import java.io.*;
import java.util.StringTokenizer;

public class no10158 {

//    public static void main(String[] args) {
//
//        Scanner sc = new Scanner(System.in);
//
//        int w = sc.nextInt();
//        int h = sc.nextInt();
//        int p = sc.nextInt();
//        int q = sc.nextInt();
//        int t = sc.nextInt();
//
//        int currentX = (p+t) % (2*w);
//        int currentY = (q+t) % (2*h);
//
//        if(currentX > w) currentX = 2*w - currentX;
//        if(currentY > h) currentY = 2*h - currentY;
//
//        System.out.println(currentX+" "+currentY);
//
//
//    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st1 = new StringTokenizer(br.readLine());
        StringTokenizer st2 = new StringTokenizer(br.readLine());

        //입력 값 세팅
        int w = Integer.parseInt(st1.nextToken());
        int h = Integer.parseInt(st1.nextToken());

        int p = Integer.parseInt(st2.nextToken());
        int q = Integer.parseInt(st2.nextToken());

        int t = Integer.parseInt(br.readLine());

        //t 시간 이후 개미의 위치 변수
        int x = (p+t) % (2*w);
        int y = (q+t) % (2*h);

        if(x > w) x = 2*w - x;
        if(y > h) y = 2*h - y;
        bw.write(String.valueOf(y));
        bw.flush();
        bw.close();
    }
}

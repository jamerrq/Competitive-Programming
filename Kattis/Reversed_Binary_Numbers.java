import java.util.Scanner;


class Reversed_Binary_Numbers{
    static String reverse(String s){
        String a = "";
        for(int i = 0; i < s.length(); i++){
            a += s.charAt(s.length() - i - 1);
        }
        return a;
    }

    static int binary(int n){
        String s = Integer.toBinaryString(n);
        s = reverse(s);
        int b = 0;
        for(int i = 0; i < s.length(); i++){b += (s.charAt(i) - '0') * Math.pow(2, s.length() - i - 1);}
        return b;
    }

    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        System.out.println(binary(n));
        s.close();
    }
}

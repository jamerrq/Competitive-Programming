import java.util.Scanner;
class Filip{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int a = s.nextInt();
        int b = s.nextInt();
        String sa = String.valueOf(a);
        String sb = String.valueOf(b);
        String c = "";
        for(int i = 0; i < sa.length(); i++)c += sa.charAt(sa.length() - i - 1);
        a = Integer.parseInt(c);
        c = "";
        for(int i = 0; i < sb.length(); i++)c += sb.charAt(sb.length() - i - 1);
        b = Integer.parseInt(c);
        System.out.println(Math.max(a,b));
    }
}

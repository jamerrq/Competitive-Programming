public class Kornislav
{
    static int area(int a, int b, int c, int d){
        int area = 0, x = 0, y = 0;
        x += a; y += b; x -= c; y -= d;
        if(x <= 0 && y <= 0)return Math.min(a, c) * Math.min(b, d);
        else return -1;
    }
    
    public static void main(String[] args){
        java.util.Scanner sc = new java.util.Scanner(System.in);
        int a = sc.nextInt(), b = sc.nextInt(), c = sc.nextInt(), d = sc.nextInt();
        int max = 0;
        //
        max = Math.max(max, area(a, b, c, d));
        max = Math.max(max, area(a, b, d, c));
        max = Math.max(max, area(a, c, b, d));
        max = Math.max(max, area(a, c, d, b));
        max = Math.max(max, area(a, d, b, c));
        max = Math.max(max, area(a, d, c, b));
        //
        max = Math.max(max, area(b, a, c, d));
        max = Math.max(max, area(b, a, d, c));
        max = Math.max(max, area(b, c, a, d));
        max = Math.max(max, area(b, c, d, a));
        max = Math.max(max, area(b, d, a, c));
        max = Math.max(max, area(b, d, c, a));
        //
        max = Math.max(max, area(c, b, a, d));
        max = Math.max(max, area(c, b, d, a));
        max = Math.max(max, area(c, a, b, d));
        max = Math.max(max, area(c, a, d, b));
        max = Math.max(max, area(c, d, b, a));
        max = Math.max(max, area(c, d, a, b));
        //
        max = Math.max(max, area(d, b, c, a));
        max = Math.max(max, area(d, b, a, c));
        max = Math.max(max, area(d, c, b, a));
        max = Math.max(max, area(d, c, a, b));
        max = Math.max(max, area(d, a, b, c));
        max = Math.max(max, area(d, a, c, b));
        //
        System.out.println(max);
    }
}

public class Spavanac
{
    public static void main(String[] args){
        java.util.Scanner sc = new java.util.Scanner(System.in);
        int h = sc.nextInt(), m = sc.nextInt();
        if(m < 45){
            if(h > 0){h -= 1;}
            else h = 23;
            m += 15;
        }else{
            m -= 45;
        }
        System.out.println(h + " " + m);
    }
}

import java.util.Scanner;
class Number_Fun{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        for(int i = 0; i < n; i++){
            int a, b, c;
            a = s.nextInt();
            b = s.nextInt();
            c = s.nextInt();
            String r = "Impossible";
            if(a + b == c || a - b == c || b - a == c || a * b == c || a * c == b || b * c == a)r = "Possible";
            System.out.println(r);
        }
    }
}

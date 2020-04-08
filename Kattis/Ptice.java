public class Ptice
{
    public static void main(String[] args){
        java.util.Scanner sc = new java.util.Scanner(System.in);
        int n = sc.nextInt();
        String s = sc.next();
        int a = 0, b = 0, g = 0;
        boolean c = false;
        for(int i = 0; i < s.length(); i++){
            if(i % 3 == 0){
                if(s.charAt(i) == 'A')a++;
            }else if(i % 3 == 1){
                if(s.charAt(i) == 'B')a++;
            }else{
                if(s.charAt(i) == 'C')a++;
            }
            if(i % 4 == 0 || i % 4 == 2){
                if(s.charAt(i) == 'B')b++;
            }else if(i % 4 == 1){
                if(s.charAt(i) == 'A')b++;
            }else{
                if(s.charAt(i) == 'C')b++;
            }
            if(i % 6 == 0 || i % 6 == 1){
                if(s.charAt(i) == 'C')g++;
            }else if(i % 6 == 2 || i % 6 == 3){
                if(s.charAt(i) == 'A')g++;
            }else{
                if(s.charAt(i) == 'B')g++;
            }           
        }
        int max = Math.max(a, Math.max(b, g));
        System.out.println(max);
        if(a == max)System.out.println("Adrian");
        if(b == max)System.out.println("Bruno");
        if(g == max)System.out.println("Goran");
    }
}

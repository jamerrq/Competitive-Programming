public class ToLower
{
    public static void main(String[] args){
        java.util.Scanner sc = new java.util.Scanner(System.in);
        int p = sc.nextInt(), t = sc.nextInt();
        int total = 0;
        for(int i = 0; i < p; i++){
            int count = 0;
            for(int j = 0; j < t; j++){
                String temp = sc.next();
                temp = temp.substring(0,1).toLowerCase() + temp.substring(1);
                if(temp.toLowerCase().equals(temp))count++;
            }
            if(count == t)total++;
        }
        System.out.println(total);
    }
}

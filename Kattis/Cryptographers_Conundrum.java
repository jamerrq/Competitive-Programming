public class Cryptographers_Conundrum
{
    public static void main(String[] args){
        java.util.Scanner sc = new java.util.Scanner(System.in);
        String message = sc.next();
        int days = 0;
        for(int i = 0; i < message.length(); i++){
            if(i % 3 == 0){
                if(message.charAt(i) != 'P')days++;
            }
            else if(i % 3 == 1){
                if(message.charAt(i) != 'E')days++;                
            }else{
                if(message.charAt(i) != 'R')days++;
            }
        }
        System.out.println(days);
    }
}

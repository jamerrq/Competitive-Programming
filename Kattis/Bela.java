public class Bela
{
    public static void main(String[] args){
        java.util.Scanner sc = new java.util.Scanner(System.in);
        int n = sc.nextInt(), sum = 0;
        String d = sc.next();
        for(int i = 0; i < 4 * n; i++){
            String card = sc.next();
            String number = card.substring(0,1); 
            String suit = card.substring(1);
            if(number.equals("A"))sum += 11;
            if(number.equals("K"))sum += 4;
            if(number.equals("Q"))sum += 3;
            if(number.equals("J")){
                if(suit.equals(d))sum += 20;
                else sum += 2;
            }
            if(number.equals("T"))sum += 10;
            if(number.equals("9") && suit.equals(d))sum += 14;
        }
        System.out.println(sum);
    }
}

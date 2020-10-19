import java.util.Scanner;
class Seven_Wonders{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        String cards = s.next();
        int t = 0, c = 0, g = 0, sum = 0;
        for(int i = 0; i < cards.length(); i++){
            if(cards.charAt(i) == 'T')t++;
            if(cards.charAt(i) == 'C')c++;
            if(cards.charAt(i) == 'G')g++;
        }
        sum += t * t;
        sum += c * c;
        sum += g * g;
        int min = Math.min(Math.min(t,c),g);
        sum += min * 7;
        System.out.println(sum);
        s.close();
    }
}

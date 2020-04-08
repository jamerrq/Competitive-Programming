public class Karte
{
    public static void main(String[] args){
        java.util.Scanner sc = new java.util.Scanner(System.in);
        String deck = sc.next(), P = "", K = "", H = "", T = "";
        boolean gresk = false;
        for(int i = 0; i < deck.length() - 2; i+=3){
            String card = deck.substring(i, i + 3);
            if(card.charAt(0) == 'P'){
                if(P.indexOf(card) == -1){
                    P += card;
                }else{
                    gresk = true;
                    break;
                }
            }
            else if(card.charAt(0) == 'K'){
                if(K.indexOf(card) == -1){
                    K += card;
                }else{
                    gresk = true;
                    break;
                }
            }
            else if(card.charAt(0) == 'H'){
                if(H.indexOf(card) == -1){
                    H += card;
                }else{
                    gresk = true;
                    break;
                }
            }else if(card.charAt(0) == 'T'){
                if(T.indexOf(card) == -1){
                    T += card;
                }else{
                    gresk = true;
                    break;
                }
            }
        }
        if(gresk)System.out.println("GRESKA");
        else System.out.println((13 - P.length() / 3) + " " + (13 - K.length() / 3) + " " + (13 - H.length() / 3) + " " + (13 - T.length() / 3));
    }
}

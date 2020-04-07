import java.util.Scanner;
class Pet{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int[] players = new int[5];
        int max = 0;
        int pos = 0;
        for(int i = 0; i < 5; i++){
            int sum = 0;
            for(int j = 0; j < 4; j++){
                int n = s.nextInt();
                players[i] += n;
            }
            if(players[i] > max){max = players[i]; pos = i;}
        }
        System.out.println(pos + 1 + " " + max);
    }
}

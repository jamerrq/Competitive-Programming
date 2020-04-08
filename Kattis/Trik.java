public class Trik
{
    public static void main(String[] args){
        java.util.Scanner sc = new java.util.Scanner(System.in);
        String s = sc.next();
        int[] board = new int[3];
        board[0] = 1;
        for(int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            if(c == 'A'){
                int temp = board[0];
                board[0] = board[1];
                board[1] = temp;
            }
            if(c == 'B'){
                int temp = board[1];
                board[1] = board[2];
                board[2] = temp;
            }
            if(c == 'C'){
                int temp = board[0];
                board[0] = board[2];
                board[2] = temp;
            }
        }
        if(board[0] == 1)System.out.println(1);
        if(board[1] == 1)System.out.println(2);
        if(board[2] == 1)System.out.println(3);
    }
}

public class Chess
{
    static int[] diagonalsNW(int x1, int y1, int x2, int y2){
        if(x1 < 65 || y1 < 1 || x1 > 72 || y1 > 8)return null;
        if(Math.abs(x2 - x1) == Math.abs(y2 - y1))return new int[]{x1, y1};
        return diagonalsNW(x1 - 1, y1 + 1, x2, y2);
    }

    static int[] diagonalsNE(int x1, int y1, int x2, int y2){
        if(x1 < 65 || y1 < 1 || x1 > 72 || y1 > 8)return null;
        if(Math.abs(x2 - x1) == Math.abs(y2 - y1))return new int[]{x1, y1};
        return diagonalsNE(x1 + 1, y1 + 1, x2, y2);
    }

    static int[] diagonalsSW(int x1, int y1, int x2, int y2){
        if(x1 < 65 || y1 < 1 || x1 > 72 || y1 > 8)return null;
        if(Math.abs(x2 - x1) == Math.abs(y2 - y1))return new int[]{x1, y1};
        return diagonalsSW(x1 - 1, y1 - 1, x2, y2);
    }

    static int[] diagonalsSE(int x1, int y1, int x2, int y2){
        if(x1 < 65 || y1 < 1 || x1 > 72 || y1 > 8)return null;
        if(Math.abs(x2 - x1) == Math.abs(y2 - y1))return new int[]{x1, y1};
        return diagonalsSE(x1 + 1, y1 - 1, x2, y2);
    }

    public static void main(String[] args){
        java.util.Scanner sc = new java.util.Scanner(System.in);
        int n = sc.nextInt();
        boolean[][] board = new boolean[8][8];
        for(int i = 0; i < 8; i++){
            for(int j = 0; j < 8; j++){
                if(i % 2 == j % 2)board[i][j] = true;
            }
        }
        // for(boolean[] b: board)System.out.println(java.util.Arrays.toString(b));
        for(int i = 0; i < n; i++){
            String mi1 = sc.next();
            int mi2 = sc.nextInt();
            String mf1 = sc.next();
            int mf2 = sc.nextInt();
            String mi = mi1 + mi2, mf = mf1 + mf2;
            boolean status = true;
            if(board[8 - (mi.charAt(1) - 48)][mi.charAt(0) - 65] !=
               board[8 - (mf.charAt(1) - 48)][mf.charAt(0) - 65]){
                status = false;
            }
            if(status){ // Same color
                if(mi2 == mf2){ // Same number
                    if(mi.charAt(0) == mf.charAt(0)){ // Same character
                        System.out.println(0 + " " + mi.charAt(0)
                                             + " " + mi.charAt(1));
                    }else{ // Different character
                        int c = (mi1.charAt(0) + mf1.charAt(0)) / 2;
                        int h = (Math.abs((mf1.charAt(0) - 65)
                                  - (mi1.charAt(0) - 65)) + 2) / 2;
                        if(mi2 > 4)h = mi2 + 1 - h;
                        else h = mi2 + h - 1;
                        System.out.println(2 + " " + mi1 + " " + mi2 + " " +
                                    (char)c + " " + h + " " + mf1 + " " + mf2);
                    }
                }else{ // Different number
                    if(mi1.charAt(0) == mf1.charAt(0)){ // Same character
                        int r = (mi2 + mf2) / 2,
                            w = (Math.abs(mf2 - mi2) + 2) / 2;
                        if(mi1.charAt(0) > 68)w = mi1.charAt(0) - w + 1;
                        else w += mi1.charAt(0) - 1;
                        System.out.println(2 + " " + mi1 + " "  + mi2 + " " +
                                   (char)w + " " + r + " " + mf1 + " " + mf2);
                    }else{ // Different character
                        if(Math.abs(mf2 - mi2) == Math.abs(mf1.charAt(0) -
                                    mi1.charAt(0))){  //Same diagonal
                            System.out.println(1 + " " + mi1 + " " + mi2
                                                + " " + mf1 + " " + mf2);
                        }else{
                           int[] diagonals = diagonalsNW(mi1.charAt(0),
                                                    mi2, mf1.charAt(0), mf2);
                            if(diagonals == null){
                                diagonals = diagonalsNE(mi1.charAt(0), mi2,
                                                        mf1.charAt(0), mf2);
                            }
                            if(diagonals == null){
                                diagonals = diagonalsSW(mi1.charAt(0), mi2,
                                                       mf1.charAt(0), mf2);
                            }
                            if(diagonals == null){
                                diagonals = diagonalsSE(mi1.charAt(0), mi2,
                                                        mf1.charAt(0), mf2);
                            }
                           System.out.println(2 + " " + mi1 + " " +
                           mi2 + " " +(char)diagonals[0] + " " + diagonals[1]
                           + " " + mf1 + " " + mf2);
                        }
                    }
                }
            }else{ // Different color
                System.out.println("Impossible");
            }
            sc.close();
        }
    }
}

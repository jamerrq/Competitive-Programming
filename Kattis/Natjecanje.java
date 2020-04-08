public class Natjecanje
{
    public static void main(String[] args){
        java.util.Scanner sc = new java.util.Scanner(System.in);
        int n = sc.nextInt(), s = sc.nextInt(), r = sc.nextInt();
        boolean[][] teams = new boolean[2][n];
        int count = s;
        for(int i = 0; i < s; i++){
            int t = sc.nextInt();
            teams[0][t - 1] = true;
        }
        for(int i = 0; i < r; i++){
            int t = sc.nextInt();
            if(teams[0][t - 1]){
                teams[0][t - 1] = false;
                count--;
            }else{
                teams[1][t - 1] = true;
            }
        }
        for(int i = 0; i < n; i++){
            if(teams[0][i]){
                if(i == 0){
                    if(teams[1][i + 1]){
                        count--;
                        teams[1][i + 1] = false;
                    }
                }else if(i != n - 1){
                    if(teams[1][i - 1]){
                        count--;
                        teams[1][i - 1] = false;
                    }else if (teams[1][i + 1]){
                        count--;
                        teams[1][i + 1] = false;
                    }
                }else{
                    if(teams[1][i - 1]){
                        count--;
                        teams[1][i - 1] = false;
                    }
                }
            }
        }
        System.out.println(count);
    }
}

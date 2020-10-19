public class Cetvrta
{
    public static void main(String[] args){
        java.util.Scanner sc = new java.util.Scanner(System.in);
        int[][] points = new int[2][4];
        for(int i = 0; i < 3; i++){
            points[0][i] = sc.nextInt();
            points[1][i] = sc.nextInt();
        }
        for(int i = 0; i < 2; i++){
            for(int j = 0; j < 3; j++){
                int count = 0;
                for(int k = 0; k < 3; k++){
                    if(points[i][j] == points[i][k])count++;
                }
                if(count == 1){
                    points[i][3] = points[i][j];
                }
            }
        }
        System.out.println(points[0][3] + " " + points[1][3]);
        sc.close();
    }
}

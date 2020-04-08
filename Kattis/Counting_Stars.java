public class Counting_Stars
{
    static void deleteStar(char[][] map, int row, int col){
        if(row >= 0 && row < map.length && col >= 0 && col < map[row].length){
            if(map[row][col] == '-'){
                map[row][col] = '#';
                deleteStar(map, row, col - 1);
                deleteStar(map, row, col + 1);
                deleteStar(map, row + 1, col);
                deleteStar(map, row - 1, col);
            }
        }
    }
    
    public static void main(String[] args){
        java.util.Scanner sc = new java.util.Scanner(System.in);
        int caseNumber = 1;
        while(sc.hasNext()){
            int m = sc.nextInt(), n = sc.nextInt();
            char[][] map = new char[m][n];
            for(int i = 0; i < m; i++){
                String line = sc.next();
                for(int j = 0; j < n; j++){
                    map[i][j] = line.charAt(j);
                }
            }
            int count = 0;
            for(int i = 0; i < m; i++){
                for(int j = 0; j < n; j++){
                    if(map[i][j] == '-'){
                        count++;
                        deleteStar(map, i, j);
                    }
                }
            }
            System.out.println("Case " + caseNumber + ": " + count);
            caseNumber++;
        }
    }
}

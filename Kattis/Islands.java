public class Islands{
	public static void tap(char[][] map, int row, int col){
		if(row >= 0 && row < map.length && col >= 0 && col < map[row].length){
			if(map[row][col] == 'L' || map[row][col] == 'C'){
				map[row][col] = 'W';
				tap(map, row, col - 1);
				tap(map, row + 1, col);
				tap(map, row, col + 1);
				tap(map, row - 1, col);
			}
		}
	}

	public static void main(String[] args){
		java.util.Scanner sc = new java.util.Scanner(System.in);
		int r = sc.nextInt(), c = sc.nextInt();
		char[][] map = new char[r][c];
		for(int i = 0; i < r; i++){
			String row = sc.next();
			for(int j = 0; j < c; j++){
				map[i][j] = row.charAt(j);
			}
		}
		int count = 0;
		for(int i = 0; i < r; i++){
			for(int j = 0; j < c; j++){
				if(map[i][j] == 'L'){
					count++;
					tap(map, i, j);
				}
			}
		}
		System.out.println(count);
		sc.close();
	}
}
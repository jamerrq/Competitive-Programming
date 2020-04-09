public class Eight_Queens{

	static boolean NW(char[][] board, int row, int col){
		if(row >= 0 && row < board.length && col >= 0 && col < board[row].length){
			if(board[row][col] == '*')return false;
			else return NW(board, row - 1, col - 1);
		}
		return true;
	}

	static boolean NE(char[][] board, int row, int col){
		if(row >= 0 && row < board.length && col >= 0 && col < board[row].length){
			if(board[row][col] == '*')return false;
			else return NE(board, row - 1, col + 1);
		}
		return true;
	}

	static boolean SW(char[][] board, int row, int col){
		if(row >= 0 && row < board.length && col >= 0 && col < board[row].length){
			if(board[row][col] == '*')return false;
			else return SW(board, row + 1, col - 1);
		}
		return true;
	}

	static boolean SE(char[][] board, int row, int col){
		if(row >= 0 && row < board.length && col >= 0 && col < board[row].length){
			if(board[row][col] == '*')return false;
			else return SE(board, row + 1, col + 1);
		}
		return true;
	}

	static boolean N(char[][] board, int row, int col){
		if(row >= 0 && row < board.length && col >= 0 && col < board[row].length){
			if(board[row][col] == '*')return false;
			else return N(board, row - 1, col);
		}
		return true;
	}

	static boolean W(char[][] board, int row, int col){
		if(row >= 0 && row < board.length && col >= 0 && col < board[row].length){
			if(board[row][col] == '*')return false;
			else return W(board, row, col - 1);
		}
		return true;
	}

	static boolean E(char[][] board, int row, int col){
		if(row >= 0 && row < board.length && col >= 0 && col < board[row].length){
			if(board[row][col] == '*')return false;
			else return E(board, row, col + 1);
		}
		return true;
	}

	static boolean S(char[][] board, int row, int col){
		if(row >= 0 && row < board.length && col >= 0 && col < board[row].length){
			if(board[row][col] == '*')return false;
			else return S(board, row + 1, col);
		}
		return true;
	}

	public static void main(String[] args){
		java.util.Scanner sc = new java.util.Scanner(System.in);
		char[][] board = new char[8][8];
		for(int i = 0; i < 8; i++){
			String row = sc.next();
			for(int j = 0; j < 8; j++){
				board[i][j] = row.charAt(j);
			}
		}
		boolean valid = true;
		boolean def = true;
		int count = 0;
		for(int i = 0; i < 8; i++){
			for(int j = 0; j < 8; j++){
				if(board[i][j] == '*'){
					count++;
					valid = NW(board, i - 1, j - 1) && NE(board, i - 1, j + 1) && SW(board, i + 1, j - 1) && SE(board, i + 1, j + 1) 
					&& N(board, i - 1, j) && W(board, i, j - 1) && E(board, i, j + 1) && S(board, i + 1, j);
					if(!valid)def = false; 
		 	 	}
			}
		}
		if(def && count == 8)System.out.println("valid");
		else System.out.println("invalid");
	}
}
